from app.config.settings import settings


print("APP:")
print(settings.app_name)
print(settings.app_env)
print(settings.debug)

print("\nOLLAMA:")
print(settings.ollama_host)
print(settings.ollama_model)

print("\nRECORDER:")
print(settings.recorder_sample_rate)
print(settings.recorder_channels)
print(settings.recorder_duration)

print("\nSTT:")
print(settings.stt_model)
print(settings.stt_device)
print(settings.stt_compute_type)

print("\nWAKE WORD:")
print(settings.wake_word)

print("\nTTS:")
print(settings.tts_model_path)