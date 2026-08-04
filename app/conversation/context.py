# app/conversation/context.py

from app.conversation.models import (
    ChatMessage,
    Role,
)
from app.conversation.state import ConversationState
from app.memory.manager import MemoryManager
from app.prompts.system_prompt import SYSTEM_PROMPT


class ContextBuilder:
    """
    Builds the complete LLM context.

    Responsibilities:
        - Add system prompt
        - Load user preferences
        - Include conversation history
    """

    def __init__(
        self,
        memory: MemoryManager,
        state: ConversationState,
    ) -> None:

        self._memory = memory
        self._state = state

    async def build(
        self,
        user_message: str,
    ) -> list[ChatMessage]:

        messages: list[ChatMessage] = []

        # -----------------------------
        # System Prompt
        # -----------------------------

        messages.append(
            ChatMessage(
                role=Role.SYSTEM,
                content=SYSTEM_PROMPT,
            )
        )

        # -----------------------------
        # User Preferences
        # -----------------------------

        language = await self._memory.get_user_preference(
            "language",
        )

        if language:

            messages.append(
                ChatMessage(
                    role=Role.SYSTEM,
                    content=(f"Preferred language: " f"{language.content}"),
                )
            )

        # -----------------------------
        # Conversation History
        # -----------------------------

        messages.extend(
            self._state.messages,
        )

        # -----------------------------
        # Current User Message
        # -----------------------------

        messages.append(
            ChatMessage(
                role=Role.USER,
                content=user_message,
            )
        )

        return messages
