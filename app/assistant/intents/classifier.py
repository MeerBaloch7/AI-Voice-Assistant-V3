from abc import ABC, abstractmethod

from .models import Intent, IntentType

class BaseIntentClassifier(ABC):
    """
    Interface for classifying user requests into high-level intents.
    """

    
    @abstractmethod
    async def classify(
        self,
        text: str,
    ) -> Intent:
        ...
    

class SimpleIntentClassifier(BaseIntentClassifier):
    """
    Temporary rule-based intent classifier.

    ```
    This is intentionally simple. It provides the routing boundary
    without coupling the assistant to a specific LLM-based classifier.
    """

    COMMAND_PREFIXES = (
        "open ",
        "close ",
        "launch ",
        "start ",
        "stop ",
        "play ",
        "pause ",
        "resume ",
        "search ",
        "remember ",
        "forget ",
        "set ",
        "turn on ",
        "turn off ",
    )

    async def classify(
        self,
        text: str,
    ) -> Intent:

        normalized = text.strip().lower()

        if not normalized:
            return Intent(
                type=IntentType.CONVERSATION,
                confidence=0.0,
            )

        if normalized.startswith(self.COMMAND_PREFIXES):
            return Intent(
                type=IntentType.COMMAND,
                confidence=0.9,
            )

        return Intent(
            type=IntentType.CONVERSATION,
            confidence=0.8,
        )

