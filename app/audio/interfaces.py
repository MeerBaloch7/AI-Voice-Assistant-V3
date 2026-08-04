from abc import ABC, abstractmethod

from app.audio.models import (
    AudioChunk,
    TranscriptionResult,
)


class BaseAudioRecorder(ABC):
    """
    Records audio from an input source.
    """

    @abstractmethod
    async def record(
        self,
    ) -> AudioChunk: ...


class BaseSpeechToTextProvider(ABC):
    """
    Converts audio into text.
    """

    @abstractmethod
    async def transcribe(
        self,
        audio: AudioChunk,
    ) -> TranscriptionResult: ...
