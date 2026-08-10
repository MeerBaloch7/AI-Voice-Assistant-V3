from dataclasses import dataclass
from enum import Enum


class IntentType(str, Enum):
    """
    High-level intent categories understood by AIVA.
    """

    CONVERSATION = "conversation"
    COMMAND = "command"


@dataclass(slots=True)
class Intent:
    """
    Represents AIVA's high-level interpretation
    of a user's request.
    """

    type: IntentType

    confidence: float = 0.0