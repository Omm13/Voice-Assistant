import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

from speech import take_command


def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def wish_user():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")

    elif hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am your voice assistant. How can I help you?")


def run_assistant():

    wish_user()

    while True:

        query = take_command()


        if "time" in query:

            current_time = datetime.datetime.now().strftime("%H:%M:%S")

            speak(f"The time is {current_time}")


        elif "joke" in query:

            joke = pyjokes.get_joke()

            speak(joke)


        elif "youtube" in query:

            speak("Opening YouTube")

            webbrowser.open(
                "https://youtube.com"
            )


        elif "exit" in query or "bye" in query:

            speak("Goodbye")

            break


        else:

            speak("I did not understand")


try:
    run_assistant()

except KeyboardInterrupt:
    print("\nAssistant stopped.")