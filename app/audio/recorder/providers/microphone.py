from pathlib import Path
import tempfile

import numpy as np
import sounddevice as sd
import soundfile as sf

from app.audio.interfaces import BaseAudioRecorder
from app.audio.models import AudioChunk


class MicrophoneRecorder(
    BaseAudioRecorder,
):
    """
    Records audio from the default microphone.
    """

    def __init__(
        self,
        sample_rate: int = 16000,
        channels: int = 1,
        duration: int = 5,
    ):
        self._sample_rate = sample_rate
        self._channels = channels
        self._duration = duration

    async def record(
        self,
    ) -> AudioChunk:

        print("🎤 Recording...")

        audio = sd.rec(
            int(self._duration * self._sample_rate),
            samplerate=self._sample_rate,
            channels=self._channels,
            dtype="float32",
        )

        sd.wait()

        temp_file = (
            Path(tempfile.gettempdir())
            / "aiva_recording.wav"
        )

        sf.write(
            temp_file,
            audio,
            self._sample_rate,
        )

        print("✅ Recording finished.")

        return AudioChunk(
            audio_path=temp_file,
            sample_rate=self._sample_rate,
            channels=self._channels,
        )