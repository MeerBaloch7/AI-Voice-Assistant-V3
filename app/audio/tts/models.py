from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class SpeechResult:
    """
    Result of a Text-to-Speech operation.
    """

    audio_path: Path

    duration: float = 0.0