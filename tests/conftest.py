# tests/conftest.py

from pathlib import Path

import pytest

from app.database import DatabaseManager

from app.conversation.context import ContextBuilder
from app.conversation.state import ConversationState

from app.memory.manager import MemoryManager

from app.memory.providers.null_semantic_provider import (
    NullSemanticProvider,
)
from app.memory.providers.sqlite_provider import SQLiteProvider

from app.memory.services import (
    PersistentMemoryService,
    SemanticMemoryService,
    WorkingMemoryService,
)

from app.memory.working.session_memory import SessionMemory

# ==================================================
# Database
# ==================================================


@pytest.fixture
def test_database(tmp_path: Path):

    db_path = tmp_path / "test_memory.db"

    database = DatabaseManager(
        database_url=f"sqlite:///{db_path}",
    )

    database.create_tables()

    return database


# ==================================================
# Providers
# ==================================================


@pytest.fixture
def sqlite_provider(
    test_database,
):

    return SQLiteProvider(
        database=test_database,
    )


@pytest.fixture
def session_memory():

    return SessionMemory()


@pytest.fixture
def semantic_provider():

    return NullSemanticProvider()


# ==================================================
# Services
# ==================================================


@pytest.fixture
def persistent_service(
    sqlite_provider,
):

    return PersistentMemoryService(
        provider=sqlite_provider,
    )


@pytest.fixture
def working_service(
    session_memory,
):

    return WorkingMemoryService(
        provider=session_memory,
    )


@pytest.fixture
def semantic_service(
    semantic_provider,
):

    return SemanticMemoryService(
        provider=semantic_provider,
    )


# ==================================================
# Managers
# ==================================================


@pytest.fixture
def memory_manager(
    persistent_service,
    working_service,
    semantic_service,
):

    return MemoryManager(
        persistent=persistent_service,
        working=working_service,
        semantic=semantic_service,
    )


# ==================================================
# Conversation
# ==================================================


@pytest.fixture
def conversation_state():

    return ConversationState()


@pytest.fixture
def context_builder(
    memory_manager,
):
    state = ConversationState()

    return ContextBuilder(
        memory=memory_manager,
        state=state,
    )
