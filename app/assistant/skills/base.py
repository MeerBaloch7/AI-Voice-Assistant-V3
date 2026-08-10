from abc import ABC, abstractmethod

from .models import SkillRequest, SkillResponse


class BaseSkill(ABC):
    """
    Base interface for all AIVA skills.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique name of the skill.
        """
        ...

    @abstractmethod
    async def execute(
        self,
        request: SkillRequest,
    ) -> SkillResponse:
        """
        Execute the skill.
        """
        ...