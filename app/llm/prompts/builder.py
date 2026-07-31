# app/llm/prompts/builder.py

from app.llm.models import (
    LLMMessage,
    LLMRequest,
)

from .system_prompt import SYSTEM_PROMPT


class PromptBuilder:

    @staticmethod
    def build(
        user_input: str,
    ) -> LLMRequest:

        messages = [

            LLMMessage(
                role="system",
                content=SYSTEM_PROMPT,
            ),

            LLMMessage(
                role="user",
                content=user_input,
            )

        ]

        return LLMRequest(
            messages=messages,
        )