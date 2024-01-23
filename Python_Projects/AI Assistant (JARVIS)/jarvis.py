import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is jarvis, ai assisstant")

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wish_me():
    speak("Welcome back Sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour <18:
        speak("Good afternoon Sir!")
    elif hour >=18 and hour <24:
        speak("Good evening Sir!")
    else:
        speak("Good night Sir!")    
    speak("jarvis at your service, please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = "en-in")
        print(query)

    except  Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return(query)    

if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
        elif "offline" in query:
            quit()  
        
    