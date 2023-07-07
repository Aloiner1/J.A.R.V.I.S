import os
import sys
import webbrowser
import speech_recognition as sr
import pyttsx3
#---------------------ON ENGINE------------------------------------------
engine = pyttsx3.init()
#---------------------ALL DEF-------------------------------------------
def talk(words):
    print(words)
    engine.say("Привет")
    engine.runAndWait()


talk("Привет, Чем могу помочь?")
#----------------------DEF RECOGNIZER----------------------------------
def command():
    r =sr.Recognizer()

    with sr.Microphone() as source:
        print('говори')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print('You: ' + task)
    except sr.UnknownValueError():
        talk('Я вас не понимаю')
        task = command()

    return task
#-----------------------DEF GOOGLE-----------------------------------------------
def make_something(ar_task):
    if ('открой' and 'сайт') in ar_task:
        talk('окей')
        url = 'https://www.google.com/webhp'
        webbrowser.open(url)

    elif 'Пока' in ar_task:
        talk('Пока')
        sys.exit()

    elif 'Имя' in ar_task:
        talk('Меня зовут Джарвис!')
#-------------------------WHILE---------------------------------------------
while True:
    make_something(command())