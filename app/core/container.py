# app/core/container.py

from app.llm.factory import LLMProviderFactory
from app.llm.manager import LLMManager


class ServiceContainer:

    def __init__(self):

        self._services = {}

    def register(
        self,
        name: str,
        service,
    ):

        self._services[name] = service

    def get(
        self,
        name: str,
    ):

        return self._services[name]

    def initialize(self):

        llm_provider = LLMProviderFactory.create()

        llm_manager = LLMManager(llm_provider)

        self.register(
            "llm",
            llm_manager,
        )