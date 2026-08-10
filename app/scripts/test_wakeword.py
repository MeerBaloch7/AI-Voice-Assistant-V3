import asyncio
from pathlib import Path

from app.audio.models import AudioChunk
from app.audio.stt.manager import SpeechToTextManager
from app.audio.stt.providers.fast_whisper_provider import (
    FasterWhisperProvider,
)
from app.audio.wakeword.providers.keyword_providers import (
    KeywordWakeWordProvider,
)


async def main():

    audio = AudioChunk(
        audio_path=Path("test.wav"),
        sample_rate=16000,
        channels=1,
    )

    # STT provider
    stt_provider = FasterWhisperProvider(
        model_name="base",
        device="cpu",
        compute_type="int8",
    )

    stt_manager = SpeechToTextManager(
        provider=stt_provider,
    )

    # Wake-word provider
    wake_word_provider = KeywordWakeWordProvider(
        stt=stt_manager,
        wake_word="hey aiva",
    )

    result = await wake_word_provider.detect(audio)

    print("Transcription:", result.transcription)
    print("Wake word detected:", result.detected)
    print("Wake word:", result.wake_word)
    print("Confidence:", result.confidence)


if __name__ == "__main__":
    asyncio.run(main())