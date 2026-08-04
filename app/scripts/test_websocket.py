import asyncio

import websockets


async def main():

    uri = "ws://127.0.0.1:8000/ws/chat"

    async with websockets.connect(uri) as ws:

        await ws.send("Hello")

        reply = await ws.recv()

        print(reply)


asyncio.run(main())