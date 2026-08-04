# app/memory/manager.py

from app.memory.services import (
    PersistentMemoryService,
    SemanticMemoryService,
    WorkingMemoryService,
)


class MemoryManager:
    """
    Facade for the application's memory subsystem.

    All application modules should communicate with memory
    through this class only.
    """

    def __init__(
        self,
        persistent: PersistentMemoryService,
        working: WorkingMemoryService,
        semantic: SemanticMemoryService,
    ) -> None:

        self._persistent = persistent
        self._working = working
        self._semantic = semantic

    # ==================================================
    # User Preferences
    # ==================================================

    async def save_user_preference(
        self,
        key: str,
        value: str,
    ) -> None:

        await self._persistent.save_user_preference(
            key=key,
            value=value,
        )

    async def get_user_preference(
        self,
        key: str,
    ):

        return await self._persistent.get_user_preference(key)

    async def delete_user_preference(
        self,
        key: str,
    ) -> None:

        await self._persistent.delete_user_preference(key)

    # ==================================================
    # Episodic Memory
    # ==================================================

    async def save_episode(
        self,
        content: str,
        importance: int = 1,
    ) -> None:

        await self._persistent.save_episode(
            content=content,
            importance=importance,
        )

    async def search_episodes(
        self,
        query: str,
        limit: int = 5,
    ):

        return await self._persistent.search_episodes(
            query=query,
            limit=limit,
        )

    # ==================================================
    # Working Memory
    # ==================================================

    async def set_working_memory(
        self,
        key: str,
        value: str,
    ) -> None:

        await self._working.set(
            key=key,
            value=value,
        )

    async def get_working_memory(
        self,
        key: str,
    ):

        return await self._working.get(key)

    async def clear_working_memory(
        self,
    ) -> None:

        await self._working.clear()

    # ==================================================
    # Semantic Memory
    # ==================================================

    async def save_semantic_memory(
        self,
        text: str,
    ) -> None:

        await self._semantic.save(text)

    async def search_semantic_memory(
        self,
        query: str,
        limit: int = 5,
    ):

        return await self._semantic.search(
            query=query,
            limit=limit,
        )
