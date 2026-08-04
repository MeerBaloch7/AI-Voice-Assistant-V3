from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):

        self._connections: list[WebSocket] = []

    async def connect(
        self,
        websocket: WebSocket,
    ):

        await websocket.accept()

        self._connections.append(
            websocket,
        )

    def disconnect(
        self,
        websocket: WebSocket,
    ):

        if websocket in self._connections:

            self._connections.remove(
                websocket,
            )

    async def send(
        self,
        websocket: WebSocket,
        message: str,
    ):

        await websocket.send_text(
            message,
        )