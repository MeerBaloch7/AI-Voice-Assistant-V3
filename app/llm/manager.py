# LLM manager and orchestration logic
from .interfaces import BaseLLMProvider
from .models import LLMRequest, LLMResponse


class LLMManager:

    def __init__(
        self,
        provider: BaseLLMProvider,
    ):
        self._provider = provider

    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:

        return await self._provider.generate(request)

    async def stream(
        self,
        request: LLMRequest,
    ):
        return self._provider.stream(request)

    async def health(self) -> bool:

        return await self._provider.health()

    async def model_name(self) -> str:

        return await self._provider.model_name()