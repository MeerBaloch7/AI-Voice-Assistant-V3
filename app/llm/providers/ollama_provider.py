from time import perf_counter

from ollama import AsyncClient

from app.config.settings import settings
from app.llm.interfaces import BaseLLMProvider
from app.llm.models import (
    LLMMessage,
    LLMRequest,
    LLMResponse,
)


from ollama import AsyncClient

class OllamaProvider:

    def __init__(
        self,
        client: AsyncClient,
        model: str,
    ):
        self.client = client
        self.model = model

    def _convert_messages(
        self,
        messages: list[LLMMessage],
    ) -> list[dict]:

        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        ]

    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        start = perf_counter()

        response = await self.client.chat(
            model=self.model,
            messages=self._convert_messages(request.messages),
            options={
                "temperature": request.temperature,
            },
        )

        latency = perf_counter() - start

        return LLMResponse(
            content=response["message"]["content"],
            model=response["model"],
            finish_reason=response.get("done_reason"),
            latency=latency,
            raw_response=response,
        )

    async def stream(
        self,
        request: LLMRequest,
    ):

        stream = await self.client.chat(
            model=self.model,
            messages=self._convert_messages(request.messages),
            stream=True,
        )

        async for chunk in stream:
            yield chunk["message"]["content"]

    async def health(
        self,
    ) -> bool:

        try:

            await self.client.ps()

            return True

        except Exception:

            return False

    async def model_name(
        self,
    ) -> str:

        return self.model