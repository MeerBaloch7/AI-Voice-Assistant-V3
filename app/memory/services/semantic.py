# app/memory/services/semantic.py

from app.memory.interfaces import BaseMemoryProvider


class SemanticMemoryService:
    """
    Handles vector memory.
    """

    def __init__(
        self,
        provider: BaseMemoryProvider,
    ):
        self._provider = provider
