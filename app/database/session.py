# app/database/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.settings import settings


def create_engine_and_session(
    database_url: str | None = None,
):
    """
    Create a SQLAlchemy engine and session factory.
    """

    engine = create_engine(
        database_url or settings.database_url,
        echo=False,
        future=True,
    )

    session_local = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False,
    )

    return engine, session_local
