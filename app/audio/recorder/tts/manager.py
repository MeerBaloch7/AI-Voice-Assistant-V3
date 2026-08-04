from .interfaces import BaseTextToSpeechProvider
from .models import SpeechResult


class TextToSpeechManager:
    """
    Facade for Text-to-Speech.
    """

    def __init__(
        self,
        provider: BaseTextToSpeechProvider,
    ):
        self._provider = provider

    async def speak(
        self,
        text: str,
    ) -> SpeechResult:

        return await self._provider.synthesize(text)