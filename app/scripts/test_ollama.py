import asyncio

from app.llm.manager import LLMManager
from app.llm.models import LLMMessage, LLMRequest
from app.llm.providers import OllamaProvider


async def main():

    provider = OllamaProvider()

    manager = LLMManager(provider)

    request = LLMRequest(
        messages=[
            LLMMessage(
                role="user", content="Hello, introduce yourself in one sentence."
            )
        ]
    )

    response = await manager.generate(request)

    print(response.content)


if __name__ == "__main__":
    asyncio.run(main())
