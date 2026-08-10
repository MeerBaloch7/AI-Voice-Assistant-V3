import asyncio
from pathlib import Path

from app.audio.models import AudioChunk
from app.audio.vad.providers.silero_provider import SileroVADProvider


async def main():

    audio_path = Path("test.wav")

    audio = AudioChunk(
        audio_path=audio_path,
        sample_rate=16000,
        channels=1,
    )

    provider = SileroVADProvider()

    result = await provider.detect(audio)

    print("Speech detected:", result.has_speech)
    print("Confidence:", result.confidence)


if __name__ == "__main__":
    asyncio.run(main())