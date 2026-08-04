# app/core/container.py

from app.conversation.context import ContextBuilder
from app.conversation.manager import ConversationManager
from app.conversation.state import ConversationState

from app.assistant.manager import AssistantManager
from app.audio.vad.manager import VoiceActivityManager
from app.audio.wakeword.manager import WakeWordManager
from app.audio.stt.manager import SpeechToTextManager

from app.database import DatabaseManager

from app.llm.factory import LLMProviderFactory
from app.llm.manager import LLMManager

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


class ServiceContainer:
    """
    Central Dependency Injection Container.

    Responsible for creating and registering all application services.
    """

    def __init__(self) -> None:
        self._services: dict[str, object] = {}

    def register(
        self,
        name: str,
        service: object,
    ) -> None:
        self._services[name] = service

    def get(
        self,
        name: str,
    ) -> object:
        return self._services[name]

    def initialize(self) -> None:

        # ==================================================
        # Database
        # ==================================================

        database = DatabaseManager()
        database.create_tables()

        # ==================================================
        # LLM
        # ==================================================

        llm_provider = LLMProviderFactory.create()

        llm_manager = LLMManager(
            provider=llm_provider,
        )

        # ==================================================
        # Memory Providers
        # ==================================================

        sqlite_provider = SQLiteProvider(
            database=database,
        )

        session_memory = SessionMemory()

        semantic_provider = NullSemanticProvider()

        # ==================================================
        # Memory Services
        # ==================================================

        persistent_memory = PersistentMemoryService(
            provider=sqlite_provider,
        )

        working_memory = WorkingMemoryService(
            provider=session_memory,
        )

        semantic_memory = SemanticMemoryService(
            provider=semantic_provider,
        )

        # ==================================================
        # Memory Manager
        # ==================================================

        memory_manager = MemoryManager(
            persistent=persistent_memory,
            working=working_memory,
            semantic=semantic_memory,
        )

        # ==================================================
        # Conversation
        # ==================================================

        conversation_state = ConversationState()

        context_builder = ContextBuilder(
            memory=memory_manager,
            state=conversation_state,
        )

        conversation_manager = ConversationManager(
            llm=llm_manager,
            memory=memory_manager,
            state=conversation_state,
            context_builder=context_builder,
        )
        #================================
        # Assistant
        #==========================
        assistant = AssistantManager(
            vad=vad_manager,
            wake_word=wake_word_manager,
            stt=stt_manager,
            conversation=conversation_manager,
        )

    

        # ==================================================
        # Register Services
        # ==================================================

        self.register("database", database)

        self.register("llm", llm_manager)

        self.register("sqlite_provider", sqlite_provider)
        self.register("session_memory", session_memory)
        self.register("semantic_provider", semantic_provider)

        self.register("persistent_memory", persistent_memory)
        self.register("working_memory", working_memory)
        self.register("semantic_memory", semantic_memory)

        self.register("memory", memory_manager)

        self.register("conversation_state", conversation_state)
        self.register("context_builder", context_builder)
        self.register("conversation", conversation_manager)

        self.register("assistant",assistant,)
