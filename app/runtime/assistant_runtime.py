#app/runtime/assistant.py

class AssistantRuntime:
    """
    Runs the voice assistant continuously.
    """

    def __init__(self, pipeline):
        self._pipeline = pipeline

    async def run(self):

        print("🤖 AIVA is running. Press Ctrl+C to stop.")

        try:
            while True:
                await self._pipeline.run_once()

        except KeyboardInterrupt:
            print("\n👋 Shutting down AIVA...")