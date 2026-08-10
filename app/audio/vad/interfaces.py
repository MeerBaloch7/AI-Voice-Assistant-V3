# app.audio.vad.interfaces.py 

from abc import ABC, abstractmethod

from app.audio.models import AudioChunk

from .models import VoiceActivityResult


class BaseVoiceActivityDetector(ABC):

    @abstractmethod
    async def detect(
        self,
        audio: AudioChunk,
    ) -> VoiceActivityResult:
        ...