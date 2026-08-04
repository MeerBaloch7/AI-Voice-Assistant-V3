# app/conversation/state.py

from dataclasses import dataclass, field
from uuid import uuid4

from app.conversation.models import (
    ChatMessage,
    ConversationHistory,
)


@dataclass(slots=True)
class ConversationState:
    """
    Holds the runtime state of the current conversation.

    This state exists only during the application's lifetime.
    """

    conversation_id: str = field(
        default_factory=lambda: str(uuid4()),
    )

    history: ConversationHistory = field(
        default_factory=ConversationHistory,
    )

    def add_message(
        self,
        message: ChatMessage,
    ) -> None:
        """
        Add a message to the current conversation.
        """
        self.history.add(message)

    def clear(
        self,
    ) -> None:
        """
        Reset the conversation state.
        """
        self.conversation_id = str(uuid4())
        self.history.clear()

    @property
    def messages(
        self,
    ) -> list[ChatMessage]:
        """
        Returns all conversation messages.
        """
        return self.history.messages

    @property
    def last_message(
        self,
    ) -> ChatMessage | None:
        """
        Returns the latest message.
        """
        return self.history.last_message
