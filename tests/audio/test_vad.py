import pytest
from pathlib import Path

from app.audio.models import AudioChunk
from app.audio.vad.manager import VoiceActivityManager
from app.audio.vad.providers.silero_provider import (
    SileroVADProvider,
)


@pytest.mark.asyncio
async def test_detect():

    manager = VoiceActivityManager(
        SileroVADProvider(),
    )

    result = await manager.detect(
        AudioChunk(
            audio_path=Path("dummy.wav"),
            sample_rate=16000,
            channels=1,
        )
    )

    assert result.has_speech is True