import asyncio

from app.audio.recorder.manager import AudioRecorderManager
from app.audio.recorder.providers.microphone import (
    MicrophoneRecorder,
)


async def main():

    recorder = AudioRecorderManager(
        MicrophoneRecorder(
            duration=5,
        )
    )

    audio = await recorder.record()

    print(audio)


if __name__ == "__main__":

    asyncio.run(main())