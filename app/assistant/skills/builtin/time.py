from datetime import datetime

from app.assistant.skills.base import BaseSkill
from app.assistant.skills.models import (
    SkillRequest,
    SkillResponse,
)


class TimeSkill(BaseSkill):
    """
    Provides the current local system time.
    """

    @property
    def name(self) -> str:
        return "time"

    async def execute(
        self,
        request: SkillRequest,
    ) -> SkillResponse:

        current_time = datetime.now().strftime("%I:%M %p")

        return SkillResponse(
            success=True,
            message=f"The current time is {current_time}.",
        )