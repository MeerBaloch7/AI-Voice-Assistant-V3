from dataclasses import dataclass
from typing import Literal

Role = Literal["system", "user", "assistant", "tool"]


@dataclass(slots=True)
class LLMMessage:
    role: Role
    content: str


@dataclass(slots=True)
class LLMRequest:
    messages: list[LLMMessage]

    temperature: float = 0.7

    max_tokens: int | None = None

    stream: bool = False


@dataclass(slots=True)
class LLMResponse:
    content: str

    model: str

    raw_response: dict | None = None

    finish_reason: str | None = None

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0

    latency: float = 0.0
