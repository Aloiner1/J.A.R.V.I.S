import os
import speech_recognition as sr
#----------------------------------------------------------------
import pyttsx3
engine = pyttsx3.init()
# engine.say("Привет")
# engine.runAndWait()
#----------------------------------------------------------------
def talk(words):
    print(words)
    #os.system("say "+ words)
    engine.say("Привет")
    engine.runAndWait()


talk("Привет, Чем могу помочь?")

def command():
    r =sr.Recognizer()

command()