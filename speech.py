import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import smtplib

#pip3 install pyttsx3
#pip3 install pywin32
#pip3 install PyAudio
#pip3 install speechRecognition
#pip3 install wikipedia

# check the
# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))

engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')   # getting details of current speaking rate
print(rate)
engine.setProperty('rate', 200)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Ankur's assistant. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    name = ""
    while True:
        query = takeCommand().lower()

#         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("What do you want to search on youtube")
            query = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'open google' in query:
            speak("What do you want to search on google")
            query = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={query}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open browser' in query:

            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        elif 'hi' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hi Sir, May I know your name")
            content = takeCommand()
            name = content
            speak(f'Hi {content}, how may I help you')

        elif 'thank you' in query or 'goodbye' in query:
            speak(f"Thank you {name}, It was nice helping you")
            break

        elif 'how are you' in query:
            speak("I am good, What about you?")

        # elif 'increase volume' in query:
        #     volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        #     speak(f"current volume is {volume}")
        #     print(type(volume))  # printing current volume level
        #     engine.setProperty('volume', 2.0)
        #     volume = engine.getProperty('volume')
        #     speak(f"current volume is {volume}")
