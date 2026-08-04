from app.audio.models import AudioChunk

from ..interfaces import BaseVoiceActivityDetector
from ..models import VoiceActivityResult


class SileroVADProvider(
    BaseVoiceActivityDetector,
):
    """
    Placeholder implementation.

    Real Silero integration will be added later.
    """

    async def detect(
        self,
        audio: AudioChunk,
    ) -> VoiceActivityResult:

        return VoiceActivityResult(
            has_speech=True,
            confidence=1.0,
        )