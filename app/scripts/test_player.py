import asyncio

from app.api.dependencies import get_container


async def main():
    container = get_container()

    tts = container.get("tts")
    player = container.get("player")

    speech = await tts.speak(
        "This is AIVA's audio player test."
    )

    print(f"Playing: {speech.audio_path}")

    await player.play(
        speech.audio_path,
    )

    print("Playback complete.")


if __name__ == "__main__":
    asyncio.run(main())