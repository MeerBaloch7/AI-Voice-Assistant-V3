from .base import BaseSkill
from .models import SkillRequest, SkillResponse


class SkillRouter:
    """
    Routes command requests to registered skills.
    """

    def __init__(
        self,
        skills: list[BaseSkill],
    ):
        self._skills = {
            skill.name: skill
            for skill in skills
        }

    def register(
        self,
        skill: BaseSkill,
    ) -> None:

        self._skills[skill.name] = skill

    def get(
        self,
        name: str,
    ) -> BaseSkill | None:

        return self._skills.get(name)

    async def execute(
        self,
        name: str,
        request: SkillRequest,
    ) -> SkillResponse:

        skill = self.get(name)

        if skill is None:
            return SkillResponse(
                success=False,
                message=f"Skill '{name}' is not available.",
            )

        return await skill.execute(request)