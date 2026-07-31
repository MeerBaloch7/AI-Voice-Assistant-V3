# app/memory/services/persistent.py

from app.memory.interfaces import BaseMemoryProvider


class PersistentMemoryService:
    """
    Handles user preferences and episodic memory.
    """

    def __init__(
        self,
        provider: BaseMemoryProvider,
    ):
        self._provider = provider