import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import pyautogui
import os
from datetime import datetime
from googletrans import Translator
import requests
from bs4 import BeautifulSoup



def speak(text):
    my_ai = pyttsx3.init()
    voices = my_ai.getProperty('voices')
    print("")
    print(f"==> Sidney The AI : {text}")
    print("")
    Id = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    my_ai.setProperty("voice", Id)
    my_ai.say(text=text)
    my_ai.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"Ani....{query}")
        return query.lower()

    except sr.UnknownValueError:
        speak("sorry but i didn't hear you")
    except sr.RequestError as e:
        speak(f"Error making the request; {e}")

def wishMe():
    hour = datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning Ani!")
    elif 12 <= hour < 18:
        speak("Good Afternoon Ani!")   
    else:
        speak("Good Evening Ani!")  
  
    assname = "Sidney 1.2"
    speak("I am your Assistant Sidney hello")
    speak(assname)

def OpenApps(query):
    speak("Ok Sir , Wait A Second!")
            
    if 'code' in query:
        os.startfile("C:\\Users\\akhil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif 'chrome' in query:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    
    elif 'mail' in query:
        webbrowser.open('https://mail.google.com/mail/u/0/')

    elif 'github' in query:
        webbrowser.open('https://github.com/')

    elif 'classroom' in query:
        webbrowser.open('https://classroom.google.com/u/0/h')

    elif 'youtube' in query:
        webbrowser.open('https://www.youtube.com')

    speak("Your Command Has Been Completed Sir!")

def screenshot():
    screenshot = pyautogui.screenshot()
    filename = 'screenshot_{}.png'.format(datetime.now().strftime('%Y%m%d_%H%M%S'))
    screenshot.save(filename)
    os.startfile(os.path.join(os.getcwd(), filename))
    speak("Here Is Your ScreenShot")


def Temp():
    search = "temperature in delhi"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temperature = data.find("div",class_ = "BNeawe").text
    speak(f"The Temperature Outside Is {temperature}")
        
def TakeHindi():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Recognizing.....")
            query = command.recognize_google(audio,language='hi')
            print(f"You Said : {query}")

        except:
            return "none"

        return query.lower()

translator = Translator()

def Tran(translator):
    speak("Tell Me The Line!")
    line = TakeHindi()
    if line:
        result = translator.translate(line)
        translated_text = result.text
        speak(translated_text)




wishMe()

while True:
    print("")
    query = takecommand()

    if "hello" in query:
        speak("Hello Ani, Welcome Back ")

    elif "how are you" in query:
        speak("I am fine thanks for asking")

    elif "who are you" in query:
        speak("my name is sidney i am ai")

    elif "time" in query:
        time = datetime.now().strftime("%H:%M")
        speak(f"the current time is {time}")    

    elif "who created you" in query:
        speak("i am created by an engineer named ani ")

    elif 'open mail' in query or 'open github' in query or 'open classroom' in query or 'open code' in query or 'open youtube' in query or 'open chrome' in query:
        OpenApps(query)

    elif "bye" in query:
        speak("ok bye Master Ani")

    elif 'wikipedia' in query:
        speak("Searching Wikipedia.....")
        query = query.replace("Sidney","")
        query = query.replace("wikipedia","")
        wiki = wikipedia.summary(query,2)
        Speak(f"According To Wikipedia : {wiki}")

    elif 'website' in query:
        speak("Ok Sir , Launching.....")
        query = query.replace("jarvis","")
        query = query.replace(" ","")
        web1 = query.replace("open","")
        web2 = 'https://www.' + web1 + '.com'
        webbrowser.open(web2)
        Speak("Launched!")
        query = query.replace("website","")

    elif 'youtube search' in query:
        speak("OK sIR , This Is What I found For Your Search!")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        web = 'https://www.youtube.com/results?search_query=' + query
        webbrowser.open(web)
        Speak("Done Sir!")

    elif 'alarm' in query:
        speak("Enter The Time !")
        time = input(": Enter The Time :")

        while True:
            Time_Ac = datetime.datetime.now()
            now = Time_Ac.strftime("%H:%M:%S")

            if now == time:
                speak("Time To Wake Up Sir!")
                playsound('iron.mp3')
                Speak("Alarm Closed!")


    elif 'google search' in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This Is What I Found On The Web!")
        pywhatkit.search(query)

        try:
            result = googleScrap.summary(query,2)
            speak(result)
            
        except:
            speak("No Speakable Data Available!")
        
    elif "bye" in query:
        speak("ok bye Master Ani")
        break

    elif 'you need a break' in query:
        speak("Ok Sir , You Can Call Me Anytime !")
        speak("Just Say Wake Up Sidney!")
        break
    
    elif 'temperature' in query:
        Temp()
 
    elif 'translate' in query:
        Tran()
        
    elif 'remember that' in query:
            remeberMsg = query.replace("remember that","")
            remeberMsg = remeberMsg.replace("Sidney","")
            speak("You Tell Me To Remind You That :"+remeberMsg)
            remeber = open('data.txt','w')
            remeber.write(remeberMsg)
            remeber.close()

    elif 'what do you remember' in query:
        remeber = open('data.txt','r')
        speak("You Tell Me That" + remeber.read())

    elif 'screenshot' in query:
            screenshot()