from app.audio.models import AudioChunk
from app.audio.vad.manager import VoiceActivityManager
from app.audio.wakeword.manager import WakeWordManager
from app.conversation.manager import ConversationManager

from .models import AssistantResponse


class AssistantManager:
    """
    Main AI Assistant orchestrator.
    """

    def __init__(
        self,
        vad: VoiceActivityManager,
        wake_word: WakeWordManager,
        conversation: ConversationManager,
    ):

        self._vad = vad
        self._wake_word = wake_word
        self._conversation = conversation

    async def process(
        self,
        audio: AudioChunk,
    ) -> AssistantResponse | None:

        activity = await self._vad.detect(audio)

        if not activity.has_speech:
            return None

        wake = await self._wake_word.detect(audio)

        if not wake.detected:
            return None
        # transcription = await self._stt.transcribe(audio)
        
        reply = await self._conversation.chat(
            #transcription.text,
            wake.transcription
        )

        return AssistantResponse(
            user_text=wake.transcription,
            assistant_text=reply,
        )