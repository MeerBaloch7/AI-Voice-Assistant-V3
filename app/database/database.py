# app/database/database.py

from contextlib import contextmanager

from sqlalchemy.orm import Session

from app.database import models  # noqa: F401
from app.database.base import Base
from app.database.session import create_engine_and_session


class DatabaseManager:
    """
    Central database access point.
    """

    def __init__(
        self,
        database_url: str | None = None,
    ) -> None:

        self.engine, self.SessionLocal = create_engine_and_session(database_url)

    def create_tables(self) -> None:

        Base.metadata.create_all(bind=self.engine)

    @contextmanager
    def session(self) -> Session:

        session = self.SessionLocal()

        try:

            yield session

            session.commit()

        except Exception:

            session.rollback()

            raise

        finally:

            session.close()
