import datetime
import webbrowser
import speech_recognition
import pyttsx3
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning sir')
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else: speak('good evening sir')
def takecommand():
    r= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('listening...')
        r.pass_threshold = 1
        audio = r.listen(source)
    try:
        print('wait for few moments')
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said, {query}\n")
    except Exception as e:
        print(e)
        speak('say that again please')
        return "none"
    return query
if __name__ == "__main__":
    wishme()
    speak('i      am      friday  ,      how       may     i       help       you')

    while True:
        query = takecommand(). lower()
        if "wikipedia" in query:
            speak('searching in wikipedia')
            query = query.replace("Wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak('according to wikepedia')
            speak('resuts')
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open duckduck' in query:
            webbrowser.open("duckduckgo.com")
        elif 'play movies' in query:
            musicdir= "E:\\movies"
            movies= os.listdir(musicdir)
            print(movies)
            os.startfile(os.path.join(musicdir,movies[28]))
        elif 'open code' in query:
            codepath= "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar"
            os.startfile(codepath)
        elif 'open chrome' in query:
            codepath1= "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
        elif 'open firefox' in query:
            codepath2= "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(codepath2)
        elif 'what is the time' in query:
            time= datetime.datetime.now().strftime("%H:%M")
            speak(time)

