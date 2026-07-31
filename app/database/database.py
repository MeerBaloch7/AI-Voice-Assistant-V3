# app/database/database.py

from contextlib import contextmanager

from sqlalchemy.orm import Session

from app.database import models  # noqa: F401
from app.database.base import Base
from app.database.session import SessionLocal, engine


class DatabaseManager:
    """
    Central database access point.
    """

    def create_tables(self) -> None:
        Base.metadata.create_all(bind=engine)

    @contextmanager
    def session(self) -> Session:
        """
        Create a database session.

        Usage:
            with database.session() as session:
                ...
        """

        session = SessionLocal()

        try:
            yield session
            session.commit()

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()