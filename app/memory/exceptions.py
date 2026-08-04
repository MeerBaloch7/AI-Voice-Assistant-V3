# app/memory/exceptions.py

from app.core.exceptions import AssistantException


class MemoryException(AssistantException):
    """Base memory exception."""


class MemoryNotFoundError(MemoryException):
    """Memory not found."""


class MemoryStorageError(MemoryException):
    """Failed to store memory."""


class MemorySearchError(MemoryException):
    """Memory search failed."""
