from app.audio.interfaces import BaseSpeechToTextProvider
from app.audio.models import (
    AudioChunk,
    TranscriptionResult,
)


class SpeechToTextManager:
    """
    Facade for Speech-to-Text providers.
    """

    def __init__(
        self,
        provider: BaseSpeechToTextProvider,
    ):
        self._provider = provider

    async def transcribe(
        self,
        audio: AudioChunk,
    ) -> TranscriptionResult:

        return await self._provider.transcribe(audio)