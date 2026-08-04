from app.audio.models import AudioChunk

from .interfaces import BaseWakeWordProvider
from .models import WakeWordResult


class WakeWordManager:

    def __init__(
        self,
        provider: BaseWakeWordProvider,
    ):
        self._provider = provider

    async def detect(
        self,
        audio: AudioChunk,
    ) -> WakeWordResult:

        return await self._provider.detect(audio)