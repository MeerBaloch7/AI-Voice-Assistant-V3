import asyncio

from app.api.dependencies import get_container


async def main():
    container = get_container()

    conversation = container.get("conversation")

    response = await conversation.chat(
        "Hello AIVA, whats is your name?"
    )

    print("AIVA:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())