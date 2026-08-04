from dataclasses import dataclass


@dataclass(slots=True)
class WakeWordResult:
    """
    Result of wake word detection.
    """

    detected: bool

    confidence: float = 0.0

    wake_word: str | None = None

    transcription: str | None = None