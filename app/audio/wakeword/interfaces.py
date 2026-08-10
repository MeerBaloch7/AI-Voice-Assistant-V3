#app/audio/wakeword/interfaces.py 

from abc import ABC, abstractmethod

from app.audio.models import AudioChunk

from .models import WakeWordResult


class BaseWakeWordProvider(ABC):

    @abstractmethod
    async def detect(
        self,
        audio: AudioChunk,
    ) -> WakeWordResult:
        ...