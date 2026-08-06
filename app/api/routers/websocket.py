from fastapi import (
    APIRouter,
    Depends,
    WebSocket,
    WebSocketDisconnect,
)

from app.api.dependencies import get_container
from app.core.container import ServiceContainer
from app.api.websocket_manager import ConnectionManager
router = APIRouter()
manager = ConnectionManager()

@router.websocket("/ws/chat")
async def websocket_chat(
    websocket: WebSocket,
    container: ServiceContainer = Depends(
        get_container,
    ),
):
    
    await manager.connect(
    websocket,
)

    conversation = container.get(
        "conversation",
    )

    try:

        while True:

            message = await websocket.receive_text()

            response = await conversation.chat(
                message,
            )

            await manager.send(
                websocket,
                response,
            )

    except WebSocketDisconnect:

        manager.disconnect(
            websocket,
        )