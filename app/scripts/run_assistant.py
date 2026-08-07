import asyncio

from app.api.dependencies import get_container


async def main():

    container = get_container()

    runtime = container.get("runtime")

    await runtime.run()


if __name__ == "__main__":
    asyncio.run(main())