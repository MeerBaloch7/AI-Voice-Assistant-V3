# tests/memory/test_session_memory.py

import pytest


@pytest.mark.asyncio
async def test_set_and_get_working_memory(
    session_memory,
):

    await session_memory.set(
        "task",
        "Memory Module",
    )

    value = await session_memory.get(
        "task",
    )

    assert value == "Memory Module"


@pytest.mark.asyncio
async def test_unknown_key_returns_none(
    session_memory,
):

    value = await session_memory.get(
        "does_not_exist",
    )

    assert value is None


@pytest.mark.asyncio
async def test_clear_working_memory(
    session_memory,
):

    await session_memory.set(
        "language",
        "Urdu",
    )

    await session_memory.clear()

    value = await session_memory.get(
        "language",
    )

    assert value is None
