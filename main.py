import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes


# Initialize voice engine
def speak(text):
    print(f"Assistant: {text}")

    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)

    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def wish_user():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am your voice assistant. How can I help you?")


def take_command():
    return input("You: ").lower()


def run_assistant():

    wish_user()

    while True:

        query = take_command()

        if "wikipedia" in query:
            speak("Searching Wikipedia")

            query = query.replace("wikipedia", "")

            try:
                result = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(result)

            except:
                speak("Sorry, I could not find information.")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "exit" in query or "bye" in query:
            speak("Goodbye")
            break

        else:
            speak("I did not understand. Please try again.")


run_assistant()