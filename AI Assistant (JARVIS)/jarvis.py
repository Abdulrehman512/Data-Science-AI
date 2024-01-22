import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is jarvis, ai assisstant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wish_me():
    speak("Welcome back Sir!")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    speak("jarvis at your service, please tell me how can i help you?")

wish_me()