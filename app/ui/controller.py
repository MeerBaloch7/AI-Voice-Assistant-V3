import asyncio

import websockets


class UIController:

    def __init__(
        self,
        window,
        url: str = "ws://127.0.0.1:8000/ws/chat",
    ):
        self._window = window
        self._url = url

    async def send_message(
        self,
        message: str,
    ):

        self._window.status.set_status(
            "Thinking..."
        )

        try:

            async with websockets.connect(
                self._url,
            ) as ws:

                await ws.send(message)

                response = await ws.recv()

                self._window.chat.add_assistant_message(
                    response,
                )

                self._window.status.set_status(
                    "Ready"
                )

        except Exception as e:

            self._window.chat.add_assistant_message(
                f"Error: {e}"
            )

            self._window.status.set_status(
                "Disconnected"
            )