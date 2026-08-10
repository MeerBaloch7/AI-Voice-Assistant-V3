from app.audio.models import AudioChunk
from app.audio.vad.manager import VoiceActivityManager
from app.audio.wakeword.manager import WakeWordManager
from app.conversation.manager import ConversationManager

from app.assistant.intents.classifier import BaseIntentClassifier
from app.assistant.intents.models import IntentType

from .models import AssistantResponse

class AssistantManager:
    """
    Main AI Assistant orchestrator.

    ```
    Responsible for:
    - Voice activity detection
    - Wake-word detection
    - Intent classification
    - Conversation routing
    """

    def __init__(
        self,
        vad: VoiceActivityManager,
        wake_word: WakeWordManager,
        conversation: ConversationManager,
        intent_classifier: BaseIntentClassifier,
    ):
        self._vad = vad
        self._wake_word = wake_word
        self._conversation = conversation
        self._intent_classifier = intent_classifier

    async def process(
        self,
        audio: AudioChunk,
    ) -> AssistantResponse | None:

        # ==================================================
        # Voice Activity Detection
        # ==================================================

        activity = await self._vad.detect(audio)

        if not activity.has_speech:
            return None

        # ==================================================
        # Wake Word Detection + Transcription
        # ==================================================

        wake = await self._wake_word.detect(audio)

        if not wake.detected:
            return None

        user_text = wake.transcription

        if not user_text:
            return None

        # ==================================================
        # Intent Classification
        # ==================================================

        intent = await self._intent_classifier.classify(
            user_text,
        )

        print(
            f"Intent: {intent.type.value} "
            f"(confidence={intent.confidence:.2f})"
        )

        # ==================================================
        # Conversation
        # ==================================================

        if intent.type == IntentType.CONVERSATION:

            reply = await self._conversation.chat(
                user_text,
            )

            return AssistantResponse(
                user_text=user_text,
                assistant_text=reply,
            )

        # ==================================================
        # Commands
        # ==================================================

        if intent.type == IntentType.COMMAND:

            # Skill router will be added here next.
            reply = (
                "I understood that as a command, "
                "but command skills are not available yet."
            )

            return AssistantResponse(
                user_text=user_text,
                assistant_text=reply,
            )

        return None
    
