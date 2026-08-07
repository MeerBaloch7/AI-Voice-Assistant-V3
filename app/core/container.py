# app/core/container.py

from pathlib import Path

# ============================
# Database
# ============================

from app.database import DatabaseManager

# ============================
# LLM
# ============================

from app.llm.factory import LLMProviderFactory
from app.llm.manager import LLMManager

# ============================
# Memory
# ============================

from app.memory.manager import MemoryManager
from app.memory.providers.sqlite_provider import SQLiteProvider
from app.memory.providers.null_semantic_provider import (
    NullSemanticProvider,
)
from app.memory.services import (
    PersistentMemoryService,
    SemanticMemoryService,
    WorkingMemoryService,
)
from app.memory.working.session_memory import SessionMemory

# ============================
# Conversation
# ============================

from app.conversation.state import ConversationState
from app.conversation.context import ContextBuilder
from app.conversation.manager import ConversationManager

# ============================
# Audio
# ============================

from app.audio.recorder.manager import AudioRecorderManager
from app.audio.recorder.providers.microphone import (
    MicrophoneRecorder,
)

from app.audio.stt.manager import SpeechToTextManager
from app.audio.stt.providers.fast_whisper_provider import (
    FasterWhisperProvider,
)

from app.audio.vad.manager import VoiceActivityManager
from app.audio.vad.providers.silero_provider import (
    SileroVADProvider,
)

from app.audio.wakeword.manager import WakeWordManager
from app.audio.wakeword.providers.keyword_providers import (
    KeywordWakeWordProvider,
)

from app.audio.tts.manager import TextToSpeechManager
from app.audio.tts.providers.piper_provider import (
    PiperProvider,
)


from app.audio.player.manager import AudioPlayerManager
from app.audio.player.providers.sounddevice_player import SoundDevicePlayer

# ============================
# Assistant
# ============================

from app.assistant.manager import AssistantManager
from app.runtime import AssistantRuntime

# ============================
# Pipeline
# ============================

from app.pipeline.voice_pipeline import VoicePipeline


class ServiceContainer:
    """
    Central Dependency Injection Container.
    """

    def __init__(self):
        self._services: dict[str, object] = {}

    def register(
        self,
        name: str,
        service: object,
    ):
        self._services[name] = service

    def get(
        self,
        name: str,
    ):
        return self._services[name]

    def initialize(self):

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

        semantic_provider = NullSemanticProvider()

        session_memory = SessionMemory()

        # ==================================================
        # Memory Services
        # ==================================================

        persistent_memory = PersistentMemoryService(
            provider=sqlite_provider,
        )

        semantic_memory = SemanticMemoryService(
            provider=semantic_provider,
        )

        working_memory = WorkingMemoryService(
            provider=session_memory,
        )

        # ==================================================
        # Memory Manager
        # ==================================================

        memory_manager = MemoryManager(
            persistent=persistent_memory,
            semantic=semantic_memory,
            working=working_memory,
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

        # ==================================================
        # Audio Providers
        # ==================================================

        recorder_provider = MicrophoneRecorder()

        stt_provider = FasterWhisperProvider()

        vad_provider = SileroVADProvider()

        tts_provider = PiperProvider(
            model_path=Path(
                "app/models/tts/en_US-lessac-medium.onnx"
            ),
        )

        # ==================================================
        # Audio Managers
        # ==================================================

        recorder_manager = AudioRecorderManager(
            provider=recorder_provider,
        )

        stt_manager = SpeechToTextManager(
            provider=stt_provider,
        )

        vad_manager = VoiceActivityManager(
            provider=vad_provider,
        )

        wake_word_manager = WakeWordManager(
            provider=KeywordWakeWordProvider(
                stt=stt_manager,
            ),
        )

        tts_manager = TextToSpeechManager(
            provider=tts_provider,
        )

        # === PLAYER =====

        player_provider = SoundDevicePlayer()

        player_manager = AudioPlayerManager(
            provider=player_provider,
        )


        # ==================================================
        # Assistant
        # ==================================================

        assistant = AssistantManager(
            vad=vad_manager,
            wake_word=wake_word_manager,
            conversation=conversation_manager,
        )

        # ==================================================
        # Voice Pipeline
        # ==================================================

        voice_pipeline = VoicePipeline(
            recorder=recorder_manager,
            assistant=assistant,
            tts=tts_manager,
            player= player_manager
        )
        #==========
        # Runtime
        #=========
        runtime = AssistantRuntime(
            pipeline=voice_pipeline,
        )

        # ==================================================
        # Register Services
        # ==================================================

        self.register("database", database)

        self.register("llm", llm_manager)

        self.register("sqlite_provider", sqlite_provider)
        self.register("semantic_provider", semantic_provider)
        self.register("session_memory", session_memory)

        self.register("persistent_memory", persistent_memory)
        self.register("semantic_memory", semantic_memory)
        self.register("working_memory", working_memory)

        self.register("memory", memory_manager)

        self.register("conversation_state", conversation_state)
        self.register("context_builder", context_builder)
        self.register("conversation", conversation_manager)

        self.register("audio_recorder", recorder_manager)
        self.register("stt", stt_manager)
        self.register("vad", vad_manager)
        self.register("wake_word", wake_word_manager)
        self.register("tts", tts_manager)

        self.register("assistant", assistant)

        self.register("voice_pipeline", voice_pipeline)

        self.register("player", player_manager)
        self.register("runtime",    runtime,)