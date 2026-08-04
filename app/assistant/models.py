from dataclasses import dataclass


@dataclass(slots=True)
class AssistantResponse:

    user_text: str

    assistant_text: str