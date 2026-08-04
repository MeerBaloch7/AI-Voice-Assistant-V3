from app.memory.interfaces import BaseWorkingMemoryProvider


class WorkingMemoryService:
    """
    Handles short-term session memory.
    """

    def __init__(
        self,
        provider: BaseWorkingMemoryProvider,
    ) -> None:
        self._provider = provider

    async def set(
        self,
        key: str,
        value: str,
    ) -> None:

        await self._provider.set(
            key=key,
            value=value,
        )

    async def get(
        self,
        key: str,
    ) -> str | None:

        return await self._provider.get(
            key,
        )

    async def clear(
        self,
    ) -> None:

        await self._provider.clear()
