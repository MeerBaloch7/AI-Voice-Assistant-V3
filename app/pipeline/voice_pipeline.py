from app.assistant.manager import AssistantManager
from app.audio.recorder.manager import AudioRecorderManager
from app.audio.tts.manager import TextToSpeechManager


class VoicePipeline:

    def __init__(
        self,
        recorder: AudioRecorderManager,
        assistant: AssistantManager,
        tts: TextToSpeechManager,
    ):
        self._recorder = recorder
        self._assistant = assistant
        self._tts = tts

    async def run_once(self):

        audio = await self._recorder.record()

        result = await self._assistant.process(audio)

        if result is None:
            print("Wake word not detected.")
            return

        print(f"You: {result.user_text}")
        print(f"AIVA: {result.assistant_text}")

        speech = await self._tts.speak(
            result.assistant_text,
        )

        audio_data, sample_rate = sf.read(
            str(speech.audio_path),
            dtype="float32",
        )

        sd.play(
            audio_data,
            sample_rate,
        )

        sd.wait()