# app/llm/factory.py

from ollama import AsyncClient

from app.config.settings import settings
from app.llm.interfaces import BaseLLMProvider
from app.llm.providers import OllamaProvider


class LLMProviderFactory:

    @staticmethod
    def create() -> BaseLLMProvider:

        client = AsyncClient(host=settings.ollama_host)

        return OllamaProvider(
            client=client,
            model=settings.ollama_model,
        )
