class FakeVAD:

    async def detect(self, audio):

        return VoiceActivityResult(True, 1.0)


class FakeWake:

    async def detect(self, audio):

        return WakeWordResult(
            detected=True,
            confidence=1.0,
            wake_word="hey aiva",
            transcription="Hello",
        )


class FakeConversation:

    async def chat(self, text):

        return "Hi!"


@pytest.mark.asyncio
async def test_process():

    manager = AssistantManager(
        vad=VoiceActivityManager(FakeVAD()),
        wake_word=WakeWordManager(FakeWake()),
        stt=None,
        conversation=FakeConversation(),
    )

    audio = AudioChunk(
        audio_path=Path("dummy.wav"),
        sample_rate=16000,
        channels=1,
    )

    response = await manager.process(audio)

    assert response.user_text == "Hello"

    assert response.assistant_text == "Hi!"

