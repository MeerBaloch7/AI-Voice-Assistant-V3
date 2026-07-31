# app/memory/interfaces.py

from abc import ABC, abstractmethod

from app.memory.models import (
    MemoryRecord,
    SearchResult,
)


class BaseMemoryProvider(ABC):
    """
    Base interface for all memory providers.
    """


class BasePersistentMemoryProvider(BaseMemoryProvider):
    """
    Interface for persistent memory providers
    (SQLite, PostgreSQL, etc.)
    """

    @abstractmethod
    async def add(
        self,
        memory: MemoryRecord,
    ) -> None:
        ...

    @abstractmethod
    async def get(
        self,
        memory_id: str,
    ) -> MemoryRecord | None:
        ...

    @abstractmethod
    async def delete(
        self,
        memory_id: str,
    ) -> None:
        ...

    @abstractmethod
    async def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:
        ...


class BaseWorkingMemoryProvider(BaseMemoryProvider):
    """
    Interface for session memory.
    """

    @abstractmethod
    async def set(
        self,
        key: str,
        value: str,
    ) -> None:
        ...

    @abstractmethod
    async def get(
        self,
        key: str,
    ) -> str | None:
        ...

    @abstractmethod
    async def clear(self) -> None:
        ...


class BaseSemanticMemoryProvider(BaseMemoryProvider):
    """
    Interface for vector databases.
    """

    @abstractmethod
    async def add(
        self,
        memory: MemoryRecord,
    ) -> None:
        ...

    @abstractmethod
    async def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:
        ...