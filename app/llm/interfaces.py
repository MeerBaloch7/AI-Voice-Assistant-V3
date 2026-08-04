from abc import ABC, abstractmethod

from .models import LLMRequest, LLMResponse


class BaseLLMProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        request: LLMRequest,
    ) -> LLMResponse:
        """
        Generate a complete response.
        """
        raise NotImplementedError

    @abstractmethod
    async def stream(
        self,
        request: LLMRequest,
    ):
        """
        Stream response chunks.
        """
        raise NotImplementedError

    @abstractmethod
    async def health(self) -> bool:
        """
        Check provider availability.
        """
        raise NotImplementedError

    @abstractmethod
    async def model_name(self) -> str:
        """
        Return active model name.
        """
        raise NotImplementedError
