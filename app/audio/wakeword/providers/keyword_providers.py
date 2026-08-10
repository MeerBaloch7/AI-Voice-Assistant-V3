# app/audio/wakeword/providers/keyword_providers.py 

from app.audio.models import AudioChunk
from app.audio.stt.manager import SpeechToTextManager

from ..interfaces import BaseWakeWordProvider
from ..models import WakeWordResult


class KeywordWakeWordProvider(
    BaseWakeWordProvider,
):
    """
    Temporary wake-word provider.

    Uses STT + keyword matching.

    Replace later with OpenWakeWord.
    """

    def __init__(
        self,
        stt: SpeechToTextManager,
        wake_word: str = "hey aiva",
    ):
        self._stt = stt
        self._wake_word = wake_word.lower()

    async def detect(
        self,
        audio: AudioChunk,
    ) -> WakeWordResult:

        result = await self._stt.transcribe(audio)

        text = result.text.lower()

        detected = self._wake_word in text

        return WakeWordResult(
            detected=detected,
            confidence=1.0 if detected else 0.0,
            wake_word=self._wake_word if detected else None,
            transcription=result.text,
        )