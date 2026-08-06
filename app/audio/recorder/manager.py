#app.audio.recorder.manger.py
from app.audio.interfaces import BaseAudioRecorder
from app.audio.models import AudioChunk


class AudioRecorderManager:
    """
    Facade for audio recording.
    """

    def __init__(
        self,
        provider: BaseAudioRecorder,
    ):
        self._provider = provider

    async def record(self) -> AudioChunk:

        return await self._provider.record()