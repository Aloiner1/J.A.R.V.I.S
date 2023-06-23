import os
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
