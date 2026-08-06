from pathlib import Path
import tempfile
import wave

from piper.voice import PiperVoice

from app.audio.tts.interfaces import BaseTextToSpeechProvider
from app.audio.tts.models import SpeechResult


class PiperProvider(BaseTextToSpeechProvider):
    """
    Piper Text-to-Speech Provider.
    """

    def __init__(
        self,
        model_path: Path,
    ):
        self._voice = PiperVoice.load(
            str(model_path),
        )

    async def synthesize(
        self,
        text: str,
    ) -> SpeechResult:

        output_file = (
            Path(tempfile.gettempdir())
            / "aiva_tts.wav"
        )

        with wave.open(
            str(output_file),
            "wb",
        ) as wav_file:

            self._voice.synthesize_wav(
                text,
                wav_file,
            )

        return SpeechResult(
            audio_path=output_file,
        )