# app/memory/providers/models.py

from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class UserMemoryModel(Base):
    """
    Stores structured user preferences and profile data.
    """

    __tablename__ = "user_memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    key: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    value: Mapped[str] = mapped_column(
        Text,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )


class EpisodicMemoryModel(Base):
    """
    Stores important events from conversations.
    """

    __tablename__ = "episodic_memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    content: Mapped[str] = mapped_column(
        Text,
    )

    importance: Mapped[int] = mapped_column(
        Integer,
        default=1,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )