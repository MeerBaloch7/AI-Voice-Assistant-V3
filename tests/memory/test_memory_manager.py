import pytest

from app.memory.manager import MemoryManager
from app.memory.providers.null_semantic_provider import NullSemanticProvider
from app.memory.providers.sqlite_provider import SQLiteProvider
from app.memory.services import (
    PersistentMemoryService,
    SemanticMemoryService,
    WorkingMemoryService,
)
from app.memory.working.session_memory import SessionMemory


@pytest.fixture
def memory_manager(test_database):

    persistent_provider = SQLiteProvider(
        database=test_database,
    )

    persistent_service = PersistentMemoryService(
        provider=persistent_provider,
    )

    working_service = WorkingMemoryService(
        provider=SessionMemory(),
    )

    semantic_service = SemanticMemoryService(
        provider=NullSemanticProvider(),
    )

    return MemoryManager(
        persistent=persistent_service,
        working=working_service,
        semantic=semantic_service,
    )


@pytest.mark.asyncio
async def test_working_memory(memory_manager):

    await memory_manager.set_working_memory(
        "username",
        "Meer",
    )

    value = await memory_manager.get_working_memory(
        "username",
    )

    assert value == "Meer"


@pytest.mark.asyncio
async def test_user_preference(memory_manager):

    await memory_manager.save_user_preference(
        "language",
        "Urdu",
    )

    memory = await memory_manager.get_user_preference(
        "language",
    )

    assert memory is not None
    assert memory.content == "Urdu"


@pytest.mark.asyncio
async def test_delete_user_preference(memory_manager):

    await memory_manager.save_user_preference(
        "language",
        "Urdu",
    )

    await memory_manager.delete_user_preference(
        "language",
    )

    memory = await memory_manager.get_user_preference(
        "language",
    )

    assert memory is None
