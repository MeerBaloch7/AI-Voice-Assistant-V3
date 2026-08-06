import asyncio
from pathlib import Path
import wave
from app.audio.tts.providers.piper_provider import PiperProvider
from app.audio.tts.models import SpeechResult


async def main():
    provider = PiperProvider(
        model_path=Path("app/models/tts/en_US-lessac-medium.onnx"),
    )

    result = await provider.synthesize(
        "Hello. My name is AIVA. Nice to meet you."
    )

    print(result.audio_path)


if __name__ == "__main__":
    asyncio.run(main())