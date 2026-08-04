from app.config.logging import app_logger
from app.core.container import ServiceContainer


class ApplicationLifecycle:

    def __init__(self):

        self.container = ServiceContainer()

    async def startup(self):

        app_logger.info("Starting AI Assistant V3...")

        self.container.initialize()

        app_logger.info("Container initialized.")

    async def shutdown(self):

        app_logger.info("Shutting down AI Assistant V3...")
