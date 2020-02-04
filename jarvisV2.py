import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
import wolframalpha

engin = pyttsx3.init('sapi5')
client = wolframalpha.Client("4R5KQX-JKYH9R2AHP")
voices = engin.getProperty('voices')
# print(voices[1].id) To chaec how many kinds of voices are available  in our system
engin.setProperty('voice', voices[1].id)
j = 'Jayesh....'


def speak(audio):
    engin.say(audio)
    engin.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!" + j)
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!" + j)
    else:
        speak("Good Evening" + j)
    #speak("Initializing for you. please, give me a moment,...........")
    speak("I am jarvis, Please tell how may I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in').lower()
        print(f"Jayesh: {query}\n")

    except Exception as e:
        speak("Sorry could not recognized your voice. Say that again please...")
        print("Sorry could not recognized your voice. Say that again please...")
        query = takeCommand()
    return query

wishMe()
speak('I would love if you call me baby')

def main():
    while True:
        query = takeCommand()
        if 'baby' in query:
            speak('Ya')
            #while True:
            #query = takeCommand()

            if 'wikipedia' in query:
                speak('Searching in wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia')
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak('ok')
                chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                link = "https://www.youtube.com"
                webbrowser.get(chrome).open(link)

            elif 'in google' in query:
                speak('ok')
                chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                #webbrowser.get(chrome).open("https://www.google.com")
                #url= "https://www.google.com"
                try:
                    from googlesearch import search
                except ImportError:
                    print("No module name 'google' found")
                query =query
                for j in search(query, tld="co.in", num=10, stop=1, pause=2):
                    print(j)
                    webbrowser.get(chrome).open(j)


            elif 'open stackoverflow' in query:
                speak('ok')
                chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                link = "https://www.stackoverflow.com"
                webbrowser.get(chrome).open(link)


            elif 'play music' in query:
                speak('ok enjoy the songs')
                music_dir = 'E:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print("The time is:", strTime)
                speak('The time is')
                speak(strTime)

            elif 'open code' in query:
                speak('ok')
                codePath = "C:\\Users\\Jayesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)


            elif 'bye' in query or ' see you later' in query or 'stop' in query or 'nothing' in query or 'abort' in query:
                speak("ok bye-bye, take care, Have a nice day, baby")
                sys.exit()

            else:
                query = query
                speak('searching...')

                try:
                    try:
                        res = client.query(query)
                        results = next(res.results).text
                        speak('Got it')
                        speak(results)
                    except:
                        results = wikipedia.summary(query, sentences=2)
                        speak("Got it")
                        speak("Wikipedia says...")
                        speak(results)
                except:
                    chrome = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
                    webbrowser.get(chrome).open("https://www.google.com")

            speak('please tell next command')
        else:
            main()
main()







