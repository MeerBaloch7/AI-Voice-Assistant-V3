from abc import ABC, abstractmethod

from .models import PlaybackResult


class BaseAudioPlayer(ABC):
    """
    Base interface for audio playback providers.
    """

    @abstractmethod
    async def play(
        self,
        audio_path: str,
    ) -> PlaybackResult:
        ...