from fastapi import APIRouter, Depends

from app.api.dependencies import get_container
from app.api.schemas import (
    ChatRequest,
    ChatResponse,
)
from app.core.container import ServiceContainer


router = APIRouter(
    prefix="/conversation",
    tags=["Conversation"],
)


@router.post(
    "/chat",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
    container: ServiceContainer = Depends(
        get_container,
    ),
):

    conversation = container.get(
        "conversation",
    )

    response = await conversation.chat(
        request.message,
    )

    return ChatResponse(
        response=response,
    )