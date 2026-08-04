# app/memory/providers/null_semantic_provider.py

from app.memory.interfaces import BaseSemanticMemoryProvider
from app.memory.models import MemoryRecord, SearchResult


class NullSemanticProvider(BaseSemanticMemoryProvider):
    """
    Temporary semantic memory provider.

    Used until ChromaDB is implemented.
    """

    async def add(
        self,
        memory: MemoryRecord,
    ) -> None:
        pass

    async def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:
        return []
