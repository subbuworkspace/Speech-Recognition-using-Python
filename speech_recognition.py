# -*- coding: utf-8 -*-
"""
Speech Recognition using Python

Author: Subrata Mondal
"""

import speech_recognition as sr


def speech_to_text():

    # Create recognizer object
    recognizer = sr.Recognizer()

    # Use microphone as audio source
    with sr.Microphone() as source:

        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")

        text = recognizer.recognize_google(audio)

        print("\nYou said:")
        print(text)

        return text

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")

    except sr.RequestError as e:
        print("Could not connect to Speech Recognition service.")
        print("Error:", e)

    return None


if __name__ == "__main__":
    speech_to_text()
