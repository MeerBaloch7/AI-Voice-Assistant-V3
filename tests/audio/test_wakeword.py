import pytest
from pathlib import Path

from app.audio.models import AudioChunk
from app.audio.models import TranscriptionResult
from app.audio.stt.manager import SpeechToTextManager

from app.audio.wakeword.manager import WakeWordManager
from app.audio.wakeword.providers.keyword_provider import (
    KeywordWakeWordProvider,
)


class FakeSTT:

    async def transcribe(
        self,
        audio,
    ):

        return TranscriptionResult(
            text="Hey AIVA",
            language="en",
            confidence=1.0,
        )


@pytest.mark.asyncio
async def test_detect():

    stt = SpeechToTextManager(
        FakeSTT(),
    )

    manager = WakeWordManager(
        KeywordWakeWordProvider(
            stt=stt,
        )
    )

    result = await manager.detect(
        AudioChunk(
            audio_path=Path("dummy.wav"),
            sample_rate=16000,
            channels=1,
        )
    )

    assert result.detected is True