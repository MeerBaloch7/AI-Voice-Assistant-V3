class AssistantException(Exception):
    """Base exception for AI Assistant."""


class ConfigException(AssistantException):
    """Configuration related errors."""


class LLMException(AssistantException):
    """LLM provider errors."""


class MemoryException(AssistantException):
    """Memory related errors."""


class DatabaseException(AssistantException):
    """Database related errors."""


class ToolException(AssistantException):
    """Tool execution errors."""


class SpeechException(AssistantException):
    """Speech processing errors."""


class ValidationException(AssistantException):
    """Validation errors."""
