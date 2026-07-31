# app/memory/models.py

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class MemoryType(str, Enum):
    WORKING = "working"
    USER = "user"
    EPISODIC = "episodic"
    SEMANTIC = "semantic"


@dataclass(slots=True)
class MemoryRecord:
    id: str = field(default_factory=lambda: str(uuid4()))
    tags: list[str] = field(default_factory=list)

    memory_type: MemoryType = MemoryType.SEMANTIC

    content: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(default_factory=datetime.utcnow)


@dataclass(slots=True)
class SearchResult:
    memory: MemoryRecord

    score: float