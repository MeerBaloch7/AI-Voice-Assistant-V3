from fastapi import APIRouter, Depends

from app.api.dependencies import get_container
from app.api.schemas import (
    PreferenceRequest,
    PreferenceResponse,
)
from app.core.container import ServiceContainer


router = APIRouter(
    prefix="/memory",
    tags=["Memory"],
)


@router.post(
    "/preference",
    response_model=PreferenceResponse,
)
async def save_preference(
    request: PreferenceRequest,
    container: ServiceContainer = Depends(
        get_container,
    ),
):

    memory = container.get(
        "memory",
    )

    await memory.save_user_preference(
        key=request.key,
        value=request.value,
    )

    return PreferenceResponse(
        key=request.key,
        value=request.value,
    )