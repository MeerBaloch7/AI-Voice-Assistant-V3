from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"


@dataclass(slots=True)
class ChatMessage:
    """
    A single message in a conversation.
    """

    role: Role
    content: str

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC),
    )


@dataclass(slots=True)
class ConversationTurn:
    """
    One complete interaction.
    """

    user_message: ChatMessage
    assistant_message: ChatMessage


@dataclass(slots=True)
class ConversationHistory:
    """
    Complete conversation history.
    """

    messages: list[ChatMessage] = field(
        default_factory=list,
    )

    def add(
        self,
        message: ChatMessage,
    ) -> None:

        self.messages.append(message)

    def clear(
        self,
    ) -> None:

        self.messages.clear()

    @property
    def last_message(
        self,
    ) -> ChatMessage | None:

        if not self.messages:
            return None

        return self.messages[-1]
