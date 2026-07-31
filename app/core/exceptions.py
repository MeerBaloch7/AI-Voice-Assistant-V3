class AssistantException(Exception):
    """Base exception for AI Assistant."""
    pass


class ConfigException(AssistantException):
    """Configuration related errors."""
    pass


class LLMException(AssistantException):
    """LLM provider errors."""
    pass


class MemoryException(AssistantException):
    """Memory related errors."""
    pass


class DatabaseException(AssistantException):
    """Database related errors."""
    pass


class ToolException(AssistantException):
    """Tool execution errors."""
    pass


class SpeechException(AssistantException):
    """Speech processing errors."""
    pass


class ValidationException(AssistantException):
    """Validation errors."""
    pass