import asyncio

from app.api.dependencies import get_container


async def main():

    container = get_container()

    pipeline = container.get(
        "voice_pipeline",
    )

    await pipeline.run_once()


if __name__ == "__main__":
    asyncio.run(main())