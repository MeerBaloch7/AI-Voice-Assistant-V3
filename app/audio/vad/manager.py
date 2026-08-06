# audio / vad/manager.py
from app.audio.models import AudioChunk

from .interfaces import BaseVoiceActivityDetector
from .models import VoiceActivityResult


class VoiceActivityManager:

    def __init__(
        self,
        provider: BaseVoiceActivityDetector,
    ):
        self._provider = provider

    async def detect(
        self,
        audio: AudioChunk,
    ) -> VoiceActivityResult:

        return await self._provider.detect(audio)