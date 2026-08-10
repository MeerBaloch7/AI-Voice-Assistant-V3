import wave

import numpy as np
import torch
from silero_vad import get_speech_timestamps, load_silero_vad

from app.audio.models import AudioChunk

from ..interfaces import BaseVoiceActivityDetector
from ..models import VoiceActivityResult


class SileroVADProvider(BaseVoiceActivityDetector):
    """
    Silero-based Voice Activity Detection provider.
    """

    def __init__(
        self,
        threshold: float = 0.5,
    ):
        self._threshold = threshold

        # Load Silero model once when the provider is created.
        self._model = load_silero_vad()

    async def detect(
        self,
        audio: AudioChunk,
    ) -> VoiceActivityResult:

        waveform = self._load_audio(
            audio.audio_path,
        )

        speech_timestamps = get_speech_timestamps(
            waveform,
            self._model,
            threshold=self._threshold,
            sampling_rate=audio.sample_rate,
        )

        has_speech = len(speech_timestamps) > 0

        confidence = 1.0 if has_speech else 0.0

        return VoiceActivityResult(
            has_speech=has_speech,
            confidence=confidence,
        )

    @staticmethod
    def _load_audio(
        audio_path,
    ) -> torch.Tensor:
        """
        Load a WAV file and convert it into
        a mono float32 tensor suitable for Silero VAD.
        """

        with wave.open(
            str(audio_path),
            "rb",
        ) as wav_file:

            channels = wav_file.getnchannels()
            sample_width = wav_file.getsampwidth()
            frames = wav_file.readframes(
                wav_file.getnframes(),
            )

        if sample_width == 2:
            audio_data = np.frombuffer(
                frames,
                dtype=np.int16,
            ).astype(np.float32)

            audio_data /= 32768.0

        elif sample_width == 4:
            audio_data = np.frombuffer(
                frames,
                dtype=np.int32,
            ).astype(np.float32)

            audio_data /= 2147483648.0

        else:
            raise ValueError(
                f"Unsupported WAV sample width: {sample_width}"
            )

        # Convert stereo/multi-channel audio to mono.
        if channels > 1:
            audio_data = audio_data.reshape(
                -1,
                channels,
            ).mean(axis=1)

        return torch.from_numpy(
            audio_data,
        )