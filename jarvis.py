import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import json

# Engine is the voice the AI would use to speak
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

pleasing = ['Thanks', 'Appreciated', 'Good Morning', 'Good Evening']
# Adding the wordlist if user is happy with the AI

def show_voice_id():
    print("The voice ID is ", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!")   

    else:
        print("Good Evening!")  
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       
    print("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    # Getting the email credentials from json file and entering the valuesover here
    with open('email.json') as f:
        data = json.load(f)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(data['email'], data['password'])
        server.sendmail(data['email'], to, content)
        server.close()

if __name__ == "__main__":
    ''' Function that wishes the user whenever the program is started '''
    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)# Can change the number of lines by changes sentences=
            speak("According to Wikipedia") 
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'Your music directory'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\'Your username'\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("Enter the emeil address of the person whom the e-meil has to be send")
    
                to = input("Enter the emeil address of the person whom the e-meil has to be send: ")

                speak("What should I say?")
                content = takeCommand()

                sendEmail(to, content):
                speak("Email has been sent!")
                print("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email")

        elif 'show voice id' in query:
            show_voice_id()
        
        elif 'return' in query:
            speak("Sleeping...")
            print("Sleeping...")
            break

        else:
            print("Sorry I couldnt do that")
            speak("Sorry I couldnt do that")
