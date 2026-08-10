import asyncio

from app.api.dependencies import get_container


async def main():
    container = get_container()

    tts = container.get("tts")

    result = await tts.speak(
        "Hello. My name is AIVA. This is a test of my voice system."
    )

    print("Generated audio:")
    print(result.audio_path)


if __name__ == "__main__":
    asyncio.run(main())