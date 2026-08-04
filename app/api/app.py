from fastapi import FastAPI

from app.api.routers import (
    conversation,
    health,
    memory,
    websocket,
)


app = FastAPI(
    title="AI Voice Assistant",
    version="1.0.0",
)


app.include_router(health.router)
app.include_router(conversation.router)
app.include_router(memory.router)
app.include_router(websocket.router)