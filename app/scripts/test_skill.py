import asyncio

from app.assistant.skills.models import SkillRequest
from app.assistant.skills.router import SkillRouter
from app.assistant.skills.builtin.time import TimeSkill


async def main():

    time_skill = TimeSkill()

    router = SkillRouter(
        skills=[
            time_skill,
        ],
    )

    request = SkillRequest(
        text="what time is it?",
    )

    response = await router.execute(
        name="time",
        request=request,
    )

    print(f"Success: {response.success}")
    print(f"Response: {response.message}")


if __name__ == "__main__":
    asyncio.run(main())