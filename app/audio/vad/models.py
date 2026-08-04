from dataclasses import dataclass


@dataclass(slots=True)
class VoiceActivityResult:
    """
    Result of voice activity detection.
    """

    has_speech: bool

    confidence: float = 0.0