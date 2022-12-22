import subprocess
import wolframalpha
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import shutil
import pyaudio





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time():
    return datetime.datetime.now().strftime("%H:%M:%S")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = ("Siri")
    speak("I am your Assistant")
    speak(assname)


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")



def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Unable to Recognize your voice.")
        print("Unable to Recognize your voice.")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()

    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")

        elif 'search'in query:
            speak("Here you go to Google\n")
            search = takeCommand()
            webbrowser.open("https://www.google.com/"+search)
        elif 'find location' in query:
            speak("Here you go to Google maps\n")
            webbrowser.open("https://www.google.com/maps/place/")

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com/")

        elif 'time' in query:
            speak(time.ctime())
            print(time.ctime())
        elif "weather" in query:
            speak("The weather today in your city")
            webbrowser.open("https://www.accuweather.com/en/eg/cairo/127164/weather-forecast/127164")

        elif "send mail" in query:
            speak("Here you go to gmail")
            webbrowser.open("https://mail.google.com/")

        elif "open amazon" in query:
            speak("Here you go to amazon")
            webbrowser.open("https://amazon.com")

        elif "open spotify" in query:
            speak("Here you go to spotify")
            webbrowser.open("https://open.spotify.com/")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "change user" in query:
            speak("What is the new user name?")
            query = query.replace("change my name to", "")
            assname = query
            query = takeCommand().lower()
            speak("Welcome" + query)

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
            continue

        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)

        elif "what are you" in query or "who are you" in query:
            speak("I am Virtual being, My name is Siri")
            speak(f"My creator is Abdullah Afifi.")

        elif 'exit' or 'bye' in query:
            speak("Thanks for giving me your time")
            exit()

        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "who I am" in query:
            speak("If you talk then definitely your human.")

        elif 'news' in query:
            speak('here are some top news from the times of india')
            webbrowser.open("https://news.google.com/home?hl=en-US&gl=US&ceid=US:en")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "what is" in query:
            query = query.replace("where is", "")
            speak("User asked to Locate")
            location = takeCommand()

            speak(location)
            webbrowser.open("https://www.google.com/webhp?g=" + location + "")

        elif "Siri" in query:
            wishMe()
            speak("Siri in your service Mister")
            speak(assname)

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "sleep" in query:
            speak("Yes Boss")
            break

 #          speak("What should i write, sir")
  #          note = takeCommand()
   #         file = open('Siri.txt', 'w')
    #      if 'yes' in snfm or 'sure' in snfm:
    #            strTime = datetime.datetime.now().strftime("% H:% M:% S")
     #           file.write(strTime)
      #          file.write(" :- ")
     #           file.write(note)
      #      else:
       #         file.write(note)


        else:
            speak("I did not get it")
            continue
