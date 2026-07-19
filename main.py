# Import necessary libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes

# Initialize the speech Engine
def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error occurred: {e}")

# Wish The User
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. How can I help you today?")

# Simulate User Voice command
def take_command():
    return input("You:  ").lower()

# Main Assistant Function
def run_assistant():
    wish_user()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\YourUsername\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that. Can you please repeat?")
    
    run_assistant()