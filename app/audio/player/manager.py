from .interfaces import BaseAudioPlayer
from .models import PlaybackResult


class AudioPlayerManager:
    """
    Facade for audio playback.
    """

    def __init__(
        self,
        provider: BaseAudioPlayer,
    ):
        self._provider = provider

    async def play(
        self,
        audio_path: str,
    ) -> PlaybackResult:

        return await self._provider.play(
            audio_path,
        )