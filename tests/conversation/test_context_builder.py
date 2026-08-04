import pytest

from app.conversation.context import ContextBuilder
from app.conversation.models import (
    ChatMessage,
    Role,
)
from app.conversation.state import ConversationState
from app.prompts.system_prompt import SYSTEM_PROMPT


@pytest.fixture
def context_builder(memory_manager):

    state = ConversationState()

    return ContextBuilder(
        memory=memory_manager,
        state=state,
    )


@pytest.mark.asyncio
async def test_build_adds_user_message(
    context_builder,
):

    messages = await context_builder.build(
        "Hello",
    )

    assert messages[-1].role == Role.USER
    assert messages[-1].content == "Hello"


@pytest.mark.asyncio
async def test_build_contains_system_prompt(
    context_builder,
):

    messages = await context_builder.build(
        "Hello",
    )

    assert messages[0].role == Role.SYSTEM
    assert messages[0].content == SYSTEM_PROMPT


@pytest.mark.asyncio
async def test_history_is_included(
    memory_manager,
):

    state = ConversationState()

    state.add_message(
        ChatMessage(
            role=Role.USER,
            content="Previous message",
        )
    )

    builder = ContextBuilder(
        memory=memory_manager,
        state=state,
    )

    messages = await builder.build(
        "Current message",
    )

    assert any(message.content == "Previous message" for message in messages)


@pytest.mark.asyncio
async def test_user_preference_is_added(
    memory_manager,
):

    await memory_manager.save_user_preference(
        "language",
        "Urdu",
    )

    builder = ContextBuilder(
        memory=memory_manager,
        state=ConversationState(),
    )

    messages = await builder.build(
        "Hello",
    )

    assert any("Urdu" in message.content for message in messages)
