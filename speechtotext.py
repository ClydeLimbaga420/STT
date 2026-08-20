import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()


def speak(text):
    print("Reply:", text)

    engine = pyttsx3.init()
    engine.setProperty("rate", 170)

    engine.say(text)
    engine.runAndWait()

    engine.stop()


while True:

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        print("Processing...")

        text = recognizer.recognize_google(
            audio,
            language="en-US"
        )

        print("User:", text)

        # Exit commands
        if text.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break

        # Temporary response
        response = "You said " + text

        speak(response)

        print("Ready for next message...")

    except sr.WaitTimeoutError:
        print("Nothing detected.")

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")

    except sr.RequestError as e:
        print("Speech recognition error:", e)

    except Exception as e:
        print("Error:", e)
