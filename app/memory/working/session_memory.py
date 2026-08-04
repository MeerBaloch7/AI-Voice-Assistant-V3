# app/memory/working/session_memory.py

from app.memory.interfaces import BaseWorkingMemoryProvider


class SessionMemory(BaseWorkingMemoryProvider):
    """
    In-memory working memory for the current session.

    This memory is cleared when the application exits.
    """

    def __init__(self) -> None:
        self._memory: dict[str, str] = {}

    async def set(
        self,
        key: str,
        value: str,
    ) -> None:
        self._memory[key] = value

    async def get(
        self,
        key: str,
    ) -> str | None:
        return self._memory.get(key)

    async def clear(self) -> None:
        self._memory.clear()
