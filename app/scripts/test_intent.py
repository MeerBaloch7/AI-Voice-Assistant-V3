import asyncio

from app.assistant.intents.classifier import SimpleIntentClassifier


async def main():

    classifier = SimpleIntentClassifier()

    test_inputs = [
        "How are you?",
        "What can you do?",
        "open chrome",
        "launch calculator",
        "remember that my favorite color is blue",
        "play music",
        "tell me a joke",
    ]

    for text in test_inputs:

        result = await classifier.classify(text)

        print(f"Input: {text}")
        print(f"Intent: {result.type.value}")
        print(f"Confidence: {result.confidence:.2f}")
        print("-" * 40)


if __name__ == "__main__":
    asyncio.run(main())