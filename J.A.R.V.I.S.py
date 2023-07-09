import os
import openai
import sys
import webbrowser
import speech_recognition as sr
import pyttsx3
#-----------------------DOTENV----------------------------------------
from dotenv import load_dotenv as ld
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    ld(dotenv_path)
#---------------------ON ENGINE------------------------------------------
engine = pyttsx3.init()
#---------------------ON OPENAI----------------------------------------
openai.api_key = os.getenv('api_key')
#---------------------DEF TALK-------------------------------------------
def talk(words):
    print(words)
    engine.say("Привет")
    engine.runAndWait()


talk("Привет, Чем могу помочь?")
#----------------------DEF AI_RESPONSE-------------------------------
def ai_response(my_task):
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role'   :'user',
                   'content':my_task}]
    )
    return completion
#----------------------DEF RECOGNIZER----------------------------------
r =sr.Recognizer()
def command():
    global r

    with sr.Microphone() as source:
        print('говори')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
        print('You: ' + task)
    except sr.UnknownValueError:
        talk('Я вас не понимаю')
        task = command()

    return task
#-----------------------DEF GOOGLE-----------------------------------------------
def make_something(ar_task):
    if ('открой' and 'сайт') in ar_task:
        talk('окей')
        url = 'https://www.google.com/webhp'
        webbrowser.open(url)

    elif 'пока' in ar_task:
        talk('Пока')
        sys.exit()

    elif 'Имя' in ar_task:
        talk('Меня зовут Джарвис!')

    else:
        #print(handle_input(input()).choices[0].message.content)
        try:
            ai_res = ai_response(ar_task).choices[0].message.content
            talk(ai_res)
        except openai.error.ServiceUnavailableError:
            talk('У меня проблема, попробуй ещё раз.')
            try:
                ai_res = ai_response(ar_task).choices[0].message.content
                talk(ai_res)
            except openai.error.ServiceUnavailableError:
                talk('Немогу дать ответ, переспроси.')
        except openai.error.RateLimitError:
            talk('повтори через 20 секунд')
            r.pause_threshold = 20
#-------------------------WHILE---------------------------------------------
while True:
    make_something(command())