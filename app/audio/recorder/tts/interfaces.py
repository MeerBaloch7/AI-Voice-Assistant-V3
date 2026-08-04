from abc import ABC, abstractmethod

from .models import SpeechResult


class BaseTextToSpeechProvider(ABC):
    """
    Base interface for all TTS providers.
    """

    @abstractmethod
    async def synthesize(
        self,
        text: str,
    ) -> SpeechResult:
        ...