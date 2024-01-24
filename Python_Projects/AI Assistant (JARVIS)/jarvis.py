import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui

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

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587) 
    server.ehlo()
    server.starttls()
    server.login("abc@gmail.com", "123")
    server.sendmail("abc@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\SC\\Pictures\\Camera Roll\\ss.png")


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

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "xyz@gmail.com"
                send_email(to,content)
                speak("Email has been sent")    
            except  Exception as e:
                print(e)
                speak("Unable to send email")   

        elif "search in chrome" in query:
            speak("What should i search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +".com")  

        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")  
        elif "restart" in query:
            os.system("shutdown /r /t 1")  

        elif "play songs" in query:
            songs_dir = "D:\\Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))    

        elif "remember that" in query:
            speak(" What should i remember?")
            data = takeCommand()
            speak("You said me to remember that" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        
        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")    

        elif "offline" in query:
            quit()  
        
    