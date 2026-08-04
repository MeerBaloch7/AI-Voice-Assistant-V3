from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class AudioChunk:
    data: bytes
    sample_rate: int
    channels: int
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )


@dataclass(slots=True)
class TranscriptionResult:
    """
    Result returned by the Speech-to-Text engine.
    """

    text: str

    language: str | None = None

    confidence: float = 0.0

    processing_time: float = 0.0
