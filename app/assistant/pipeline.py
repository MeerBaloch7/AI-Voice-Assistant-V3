while True:

    audio = await recorder.record()

    response = await assistant.process(audio)

    if response:
        await tts.speak(
            response.assistant_text
        )