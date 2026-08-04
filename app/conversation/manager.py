# app/conversation/manager.py

from app.conversation.context import ContextBuilder
from app.conversation.models import (
    ChatMessage,
    Role,
)
from app.conversation.state import ConversationState
from app.llm.manager import LLMManager
from app.memory.manager import MemoryManager
from app.config.constants import DEFAULT_EPISODE_IMPORTANCE


class ConversationManager:
    """
    Main conversation orchestrator.

    Responsibilities:
        - Build LLM context
        - Call LLM
        - Update conversation state
        - Store memories
    """

    def __init__(
        self,
        llm: LLMManager,
        memory: MemoryManager,
        state: ConversationState,
        context_builder: ContextBuilder,
    ) -> None:

        self._llm = llm
        self._memory = memory
        self._state = state
        self._context_builder = context_builder

    async def chat(
        self,
        user_input: str,
    ) -> str:

        # ---------------------------------
        # Build Prompt
        # ---------------------------------

        messages = await self._context_builder.build(
            user_input,
        )

        # ---------------------------------
        # LLM Response
        # ---------------------------------

        response = await self._llm.generate(
            messages,
        )

        # ---------------------------------
        # Update Conversation State
        # ---------------------------------

        self._state.add_message(
            ChatMessage(
                role=Role.USER,
                content=user_input,
            )
        )

        self._state.add_message(
            ChatMessage(
                role=Role.ASSISTANT,
                content=response,
            )
        )

        # ---------------------------------
        # Save Episode
        # ---------------------------------

        await self._memory.save_episode(
            content=(f"User: {user_input}\n" f"Assistant: {response}"),
            importance=DEFAULT_EPISODE_IMPORTANCE,
        )

        return response
