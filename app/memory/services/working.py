# app/memory/services/working.py

from app.memory.interfaces import BaseMemoryProvider


class WorkingMemoryService:
    """
    Handles short-term session memory.
    """

    def __init__(
        self,
        provider: BaseMemoryProvider,
    ):
        self._provider = provider