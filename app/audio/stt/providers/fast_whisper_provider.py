import time

from faster_whisper import WhisperModel

from app.audio.interfaces import BaseSpeechToTextProvider
from app.audio.models import (
    AudioChunk,
    TranscriptionResult,
)


class FasterWhisperProvider(
    BaseSpeechToTextProvider,
):
    """
    Faster-Whisper implementation.
    """

    def __init__(
        self,
        model_name: str = "base",
        device: str = "cpu",
        compute_type: str = "int8",
    ):

        self._model = WhisperModel(
            model_name,
            device=device,
            compute_type=compute_type,
        )

    async def transcribe(
        self,
        audio: AudioChunk,
    ) -> TranscriptionResult:

        start = time.perf_counter()

        segments, info = self._model.transcribe(
            str(audio.audio_path),
        )

        text = " ".join(
            segment.text
            for segment in segments
        ).strip()

        return TranscriptionResult(
            text=text,
            language=info.language,
            confidence=info.language_probability,
            processing_time=time.perf_counter() - start,
        )