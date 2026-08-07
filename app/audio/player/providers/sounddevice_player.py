from pathlib import Path
import time

import sounddevice as sd
import soundfile as sf

from app.audio.player.interfaces import BaseAudioPlayer
from app.audio.player.models import PlaybackResult


class SoundDevicePlayer(
    BaseAudioPlayer,
):
    """
    Plays WAV audio using sounddevice.
    """

    async def play(
        self,
        audio_path: str,
    ) -> PlaybackResult:

        start = time.perf_counter()

        data, sample_rate = sf.read(
            audio_path,
            dtype="float32",
        )

        sd.play(
            data,
            sample_rate,
        )

        sd.wait()

        return PlaybackResult(
            audio_path=Path(audio_path),
            duration=time.perf_counter() - start,
        )