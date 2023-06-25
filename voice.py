import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    print('--------------------------------')
    print(f"Name:  + {voice.name}")
    print(f"ID:  + {voice.id}")
    print(f"Languages:  + {voice.languages}")
    print(f"Gender:   + {voice.gender}")
    print(f"Age:  + {voice.age}")

engine.setProperty('voices', 'eng')
for voice in voices:
    if voice.name == 'Zira':
        engine.setProperty('voice', voice.id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-40)
engine.say('Obama')
engine.runAndWait()