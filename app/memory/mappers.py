# app/memory/mappers.py

from app.memory.models import (
    MemoryRecord,
    MemoryType,
)
from app.memory.providers.models import (
    EpisodicMemoryModel,
    UserMemoryModel,
)


class MemoryMapper:
    """
    Maps ORM models to domain models and vice versa.
    """

    @staticmethod
    def to_user_record(
        model: UserMemoryModel,
    ) -> MemoryRecord:

        return MemoryRecord(
            memory_type=MemoryType.USER,
            content=model.value,
            metadata={
                "key": model.key,
            },
        )

    @staticmethod
    def to_episode_record(
        model: EpisodicMemoryModel,
    ) -> MemoryRecord:

        return MemoryRecord(
            memory_type=MemoryType.EPISODIC,
            content=model.content,
            metadata={
                "importance": model.importance,
            },
        )

    @staticmethod
    def to_user_model(
        memory: MemoryRecord,
    ) -> UserMemoryModel:

        return UserMemoryModel(
            key=memory.metadata["key"],
            value=memory.content,
        )

    @staticmethod
    def to_episode_model(
        memory: MemoryRecord,
    ) -> EpisodicMemoryModel:

        return EpisodicMemoryModel(
            content=memory.content,
            importance=memory.metadata.get(
                "importance",
                1,
            ),
        )