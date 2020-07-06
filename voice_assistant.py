import time
import os
import speech_recognition as sr
import playsound
from gtts import gTTS


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception:" + str(e))

    return said


print("Hey there! Please let me help you,say something.")

text = get_audio()
if "hello" in text:
    speak("what the fuck")

if "what is your name" in text:
     speak("my name is paldemi")
