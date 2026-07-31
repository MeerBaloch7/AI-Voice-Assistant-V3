# app/memory/manager.py

from app.memory.interfaces import BaseMemoryProvider
from app.memory.models import MemoryRecord, SearchResult


class MemoryManager:
    """
    Public entry point for the Memory Layer.
    """

    def __init__(
        self,
        working_memory: BaseMemoryProvider,
        persistent_memory: BaseMemoryProvider,
        semantic_memory: BaseMemoryProvider,
    ):
        self._working = working_memory
        self._persistent = persistent_memory
        self._semantic = semantic_memory

    async def remember(self, memory: MemoryRecord) -> None:

        match memory.memory_type:

            case memory.memory_type.WORKING:
                await self._working.add(memory)

            case memory.memory_type.USER | memory.memory_type.EPISODIC:
                await self._persistent.add(memory)

            case memory.memory_type.SEMANTIC:
                await self._semantic.add(memory)

    async def recall(
        self,
        memory_id: str,
    ) -> MemoryRecord | None:

        memory = await self._working.get(memory_id)

        if memory:
            return memory

        memory = await self._persistent.get(memory_id)

        if memory:
            return memory

        return await self._semantic.get(memory_id)

    async def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:

        return await self._semantic.search(
            query=query,
            limit=limit,
        )

    async def clear_session(self):

        self._working.clear()