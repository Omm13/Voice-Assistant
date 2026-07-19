import sounddevice as sd
import speech_recognition as sr
import numpy as np
import soundfile as sf
import time


MICROPHONE_ID = 2


def take_command():

    samplerate = 44100
    silence_limit = 2
    threshold = 200

    print("Listening...")


    audio_data = []

    silent_chunks = 0
    chunk_duration = 0.1

    chunk_size = int(samplerate * chunk_duration)

    recording_started = False

    with sd.InputStream(
        samplerate=samplerate,
        channels=1,
        device=MICROPHONE_ID,
        dtype="int16"
    ) as stream:


        while True:

            chunk, overflow = stream.read(chunk_size)

            volume = np.abs(chunk).mean()


            if volume > threshold:

                recording_started = True

                audio_data.append(chunk)

                silent_chunks = 0

            else:

                if recording_started:
                    silent_chunks += 1


            if silent_chunks > silence_limit / chunk_duration:

                if len(audio_data) > samplerate * 0.8 / chunk_size:
                    break



    audio = np.concatenate(audio_data)


    filename = "input.wav"

    sf.write(
        filename,
        audio,
        samplerate
    )

    print("Recorded duration:", len(audio)/samplerate, "seconds")

    recognizer = sr.Recognizer()


    with sr.AudioFile(filename) as source:

        audio_file = recognizer.record(source)


    try:

        print("Recognizing...")

        text = recognizer.recognize_google(audio_file)

        print("You:", text)

        return text.lower()


    except sr.UnknownValueError:

        print("Sorry, I could not understand.")

        return ""


    except sr.RequestError:

        print("Speech service unavailable.")

        return ""