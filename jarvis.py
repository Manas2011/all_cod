import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('misteranonymous185@gmail.com', 'covid2020')
    server.sendmail('misteranonymous185@gmail.com', to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("lodo lagan ")
    speak("I am Jarvis . Please tell me how may i help you")


def takeCommand():
    # it takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", "\n", query)

    except Exception as e:
        # print(e)
        print('Say that again please....')
        speak('Say that again please.....')
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for executing task
        if 'wikipedia' in query:
            speak('Searching wikipedia ............')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open physics wala' in query:
            webbrowser.open('https://physicswallah.live/landing-page')
        elif 'play music' in query:
            music_dir = "C:\\Users\\MANAS PANT\\Desktop\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time is (strTime)")
        elif 'open code' in query:
            codepath = "C:\\Users\\MANAS PANT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = "mohitsinghfaraswan215@gmail.com"
                sendEmail(to, content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry my friend Manas ! I am not able to send tHIS email')
