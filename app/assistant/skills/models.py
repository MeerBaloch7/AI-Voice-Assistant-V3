from dataclasses import dataclass


@dataclass(slots=True)
class SkillRequest:
    """
    Request passed to a skill.
    """

    text: str


@dataclass(slots=True)
class SkillResponse:
    """
    Result returned by a skill.
    """

    success: bool

    message: str