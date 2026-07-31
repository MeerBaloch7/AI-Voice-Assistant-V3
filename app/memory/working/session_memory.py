# app/memory/working/session_memory.py

from app.memory.models import MemoryRecord
from app.memory.interfaces import BaseWorkingMemoryProvider

class SessionMemory(BaseWorkingMemoryProvider):
    """
    In-memory storage for the current session.

    Data is lost when the application stops.
    """

    def __init__(self):
        self._memories: dict[str, MemoryRecord] = {}

    def add(self, memory: MemoryRecord) -> None:
        self._memories[memory.id] = memory

    def get(self, memory_id: str) -> MemoryRecord | None:
        return self._memories.get(memory_id)

    def all(self) -> list[MemoryRecord]:
        return list(self._memories.values())

    def delete(self, memory_id: str) -> bool:
        return self._memories.pop(memory_id, None) is not None

    def clear(self) -> None:
        self._memories.clear()

    def count(self) -> int:
        return len(self._memories)