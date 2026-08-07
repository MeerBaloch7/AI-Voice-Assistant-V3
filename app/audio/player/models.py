from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PlaybackResult:
    """
    Result of an audio playback operation.
    """

    audio_path: Path

    duration: float = 0.0