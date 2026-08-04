import pytest

from app.memory.services.persistent import PersistentMemoryService


@pytest.fixture
def persistent_service(sqlite_provider):
    return PersistentMemoryService(
        provider=sqlite_provider,
    )


@pytest.mark.asyncio
async def test_save_user_preference(
    persistent_service,
):
    await persistent_service.save_user_preference(
        key="language",
        value="Urdu",
    )

    result = await persistent_service.get_user_preference(
        "language",
    )

    assert result is not None
    assert result.content == "Urdu"


@pytest.mark.asyncio
async def test_update_user_preference(
    persistent_service,
):
    await persistent_service.save_user_preference(
        key="language",
        value="Urdu",
    )

    await persistent_service.save_user_preference(
        key="language",
        value="English",
    )

    result = await persistent_service.get_user_preference(
        "language",
    )

    assert result is not None
    assert result.content == "English"


@pytest.mark.asyncio
async def test_delete_user_preference(
    persistent_service,
):
    await persistent_service.save_user_preference(
        key="language",
        value="Urdu",
    )

    await persistent_service.delete_user_preference(
        "language",
    )

    result = await persistent_service.get_user_preference(
        "language",
    )

    assert result is None
