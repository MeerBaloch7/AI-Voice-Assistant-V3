import pytest

from app.conversation.models import (
    ChatMessage,
    Role,
)
from app.conversation.state import ConversationState


@pytest.fixture
def state():

    return ConversationState()


def test_add_message(state):

    message = ChatMessage(
        role=Role.USER,
        content="Hello",
    )

    state.add_message(message)

    assert len(state.messages) == 1
    assert state.last_message == message


def test_clear_state(state):

    state.add_message(
        ChatMessage(
            role=Role.USER,
            content="Hello",
        )
    )

    old_id = state.conversation_id

    state.clear()

    assert len(state.messages) == 0
    assert state.conversation_id != old_id
