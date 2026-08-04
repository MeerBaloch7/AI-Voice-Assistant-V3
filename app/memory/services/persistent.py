from app.memory.interfaces import BasePersistentMemoryProvider
from app.memory.models import (
    MemoryRecord,
    MemoryType,
)


class PersistentMemoryService:
    """
    Handles all persistent memory operations.
    """

    def __init__(
        self,
        provider: BasePersistentMemoryProvider,
    ):
        self._provider = provider

    # --------------------------------------------------
    # User Preferences
    # --------------------------------------------------

    async def save_user_preference(
        self,
        key: str,
        value: str,
    ) -> None:

        await self._provider.upsert_user_preference(
            key=key,
            value=value,
        )

    async def get_user_preference(
        self,
        key: str,
    ) -> MemoryRecord | None:

        return await self._provider.get_user_by_key(
            key,
        )

    async def delete_user_preference(
        self,
        key: str,
    ) -> None:

        await self._provider.delete_user_by_key(
            key,
        )

    # --------------------------------------------------
    # Episodic Memory
    # --------------------------------------------------

    async def save_episode(
        self,
        content: str,
        importance: int = 1,
    ) -> None:

        memory = MemoryRecord(
            memory_type=MemoryType.EPISODIC,
            content=content,
            metadata={
                "importance": importance,
            },
        )

        await self._provider.add(memory)

    async def search_episodes(
        self,
        query: str,
        limit: int = 5,
    ):

        return await self._provider.search(
            query=query,
            limit=limit,
        )
