# app/memory/providers/sqlite_provider.py

from sqlalchemy import or_, select

from app.database.database import DatabaseManager
from app.memory.interfaces import BasePersistentMemoryProvider
from app.memory.mappers import MemoryMapper
from app.memory.models import (
    MemoryRecord,
    MemoryType,
    SearchResult,
)
from app.memory.providers.models import (
    EpisodicMemoryModel,
    UserMemoryModel,
)


class SQLiteProvider(BasePersistentMemoryProvider):
    """
    SQLite implementation of the persistent memory provider.
    """

    def __init__(
        self,
        database: DatabaseManager,
    ):
        self._database = database

    async def add(
        self,
        memory: MemoryRecord,
    ) -> None:

        with self._database.session() as session:

            if memory.memory_type == MemoryType.USER:

                model = MemoryMapper.to_user_model(memory)

            elif memory.memory_type == MemoryType.EPISODIC:

                model = MemoryMapper.to_episode_model(memory)

            else:
                raise ValueError(f"Unsupported memory type: {memory.memory_type}")

            session.add(model)

    async def get(
        self,
        memory_id: str,
    ) -> MemoryRecord | None:

        with self._database.session() as session:

            user = session.get(
                UserMemoryModel,
                int(memory_id),
            )

            if user:
                return MemoryMapper.to_user_record(user)

            episode = session.get(
                EpisodicMemoryModel,
                int(memory_id),
            )

            if episode:
                return MemoryMapper.to_episode_record(episode)

        return None

    async def delete(
        self,
        memory_id: str,
    ) -> None:

        with self._database.session() as session:

            user = session.get(
                UserMemoryModel,
                int(memory_id),
            )

            if user:
                session.delete(user)
                return

            episode = session.get(
                EpisodicMemoryModel,
                int(memory_id),
            )

            if episode:
                session.delete(episode)
                return

    async def search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[SearchResult]:

        results: list[SearchResult] = []

        with self._database.session() as session:

            users = session.scalars(
                select(UserMemoryModel)
                .where(
                    or_(
                        UserMemoryModel.key.contains(query),
                        UserMemoryModel.value.contains(query),
                    )
                )
                .limit(limit)
            ).all()

            for user in users:
                results.append(
                    SearchResult(
                        memory=MemoryMapper.to_user_record(user),
                        score=1.0,
                    )
                )

            episodes = session.scalars(
                select(EpisodicMemoryModel)
                .where(EpisodicMemoryModel.content.contains(query))
                .limit(limit)
            ).all()

            for episode in episodes:
                results.append(
                    SearchResult(
                        memory=MemoryMapper.to_episode_record(episode),
                        score=1.0,
                    )
                )

        return results

    async def get_user_by_key(
        self,
        key: str,
    ) -> MemoryRecord | None:

        with self._database.session() as session:

            statement = select(UserMemoryModel).where(UserMemoryModel.key == key)

            model = session.scalar(statement)

            if model is None:
                return None

            return MemoryMapper.to_user_record(model)

    async def upsert_user_preference(
        self,
        key: str,
        value: str,
    ) -> None:

        with self._database.session() as session:

            model = (
                session.query(UserMemoryModel)
                .filter(UserMemoryModel.key == key)
                .first()
            )

            if model is None:

                model = UserMemoryModel(
                    key=key,
                    value=value,
                )

                session.add(model)

            else:

                model.value = value

    async def delete_user_by_key(
        self,
        key: str,
    ) -> None:

        with self._database.session() as session:
            statement = select(UserMemoryModel).where(UserMemoryModel.key == key)
            model = session.scalar(statement)

            if model:

                session.delete(model)
