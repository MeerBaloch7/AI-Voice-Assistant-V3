import sounddevice as sd
import soundfile as sf


SAMPLE_RATE = 16000
CHANNELS = 1
DURATION = 3
OUTPUT_FILE = "hey_aiva.wav"


print("🎙 Recording starts in 2 seconds...")
sd.sleep(2000)

print('🔴 Say: "Hey AIVA"')

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    dtype="float32",
)

sd.wait()

sf.write(
    OUTPUT_FILE,
    audio,
    SAMPLE_RATE,
)

print(f"✅ Recording saved: {OUTPUT_FILE}")