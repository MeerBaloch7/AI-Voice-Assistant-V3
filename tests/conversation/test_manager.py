class FakeLLMManager:

    async def generate(
        self,
        messages,
    ) -> str:

        return "Hello from AI"


import pytest

from app.conversation.context import ContextBuilder
from app.conversation.manager import ConversationManager
from app.conversation.state import ConversationState


@pytest.fixture
def conversation_manager(
    memory_manager,
):

    state = ConversationState()

    builder = ContextBuilder(
        memory=memory_manager,
        state=state,
    )

    manager = ConversationManager(
        llm=FakeLLMManager(),
        memory=memory_manager,
        state=state,
        context_builder=builder,
    )

    return manager, state, memory_manager


@pytest.mark.asyncio
async def test_chat_returns_response(
    conversation_manager,
):

    manager, _, _ = conversation_manager

    response = await manager.chat(
        "Hello",
    )

    assert response == "Hello from AI"


@pytest.mark.asyncio
async def test_chat_updates_history(
    conversation_manager,
):

    manager, state, _ = conversation_manager

    await manager.chat(
        "Hello",
    )

    assert len(state.messages) == 2

    assert state.messages[0].content == "Hello"

    assert state.messages[1].content == "Hello from AI"


@pytest.mark.asyncio
async def test_chat_saves_episode(
    conversation_manager,
):

    manager, _, memory = conversation_manager

    await manager.chat(
        "Hello",
    )

    results = await memory.search_episodes(
        "Hello",
    )

    assert len(results) == 1
