import pytest


@pytest.mark.asyncio
async def test_save_and_get_user_preference(sqlite_provider):

    await sqlite_provider.upsert_user_preference(
        key="language",
        value="Urdu",
    )

    memory = await sqlite_provider.get_user_by_key(
        "language",
    )

    assert memory is not None
    assert memory.content == "Urdu"


@pytest.mark.asyncio
async def test_update_user_preference(sqlite_provider):

    await sqlite_provider.upsert_user_preference(
        "language",
        "Urdu",
    )

    await sqlite_provider.upsert_user_preference(
        "language",
        "English",
    )

    memory = await sqlite_provider.get_user_by_key(
        "language",
    )

    assert memory.content == "English"


@pytest.mark.asyncio
async def test_delete_user_preference(sqlite_provider):

    await sqlite_provider.upsert_user_preference(
        "language",
        "Urdu",
    )

    await sqlite_provider.delete_user_by_key(
        "language",
    )

    memory = await sqlite_provider.get_user_by_key(
        "language",
    )

    assert memory is None
