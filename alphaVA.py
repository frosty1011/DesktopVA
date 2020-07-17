import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    

def takeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1 #seconds before a phrase is stated as completed,(If more than 1 secomnd istaken for me to pseak,it will be consider as ciopleted)
        audio = r.listen(source) 

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        

    except Exception as e:
        print(e)
        print("say that again ...")
        return "None"
    return query

if __name__ == "__main__":
    while 1:
        wishME()
        speak("I am Alpha . How may I help you")
        query=takeCommand().lower() #So that we dont get in any case confusion i.e. google or Google
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia")
            query = query.replace("Wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
            print(results)

        elif 'exit' in query:
            break
        
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif "play music" in query:
            music_dir ='C:\\Users\\nehul\\Downloads'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[3]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif "open code" in query:
            cp="D:\\Microsoft VS Code\\Code.exe"
            os.startfile(cp)




