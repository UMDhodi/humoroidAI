from os import startfile
import pyttsx3
import speech_recognition as sr
from instaloader.exceptions import QueryReturnedBadRequestException
from pyautogui import click, dragRel, press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate',160)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand(self):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 5
        audio = r.listen(source,timeout=4, phrase_time_limit=5)
        try:
            print("Recognizing...\n")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice...")
            return "none"
        return query
        
def WhatsappMsg(name, message):
    startfile("C:\\Users\\mayan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=201, y=109)                                             #tab to search bar

    sleep(1)
    write(name)

    sleep(1)
    click(x=203, y=238)                                             #click the user

    sleep(1)
    click(x=800, y=657)                                             #click message box

    sleep(1)
    write(message)
    press('enter')

def WhatsappCall(name):
    startfile("C:\\Users\\mayan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=201, y=109)                                            #tab to search bar

    sleep(1)
    write(name)

    sleep(1)
    click(x=203, y=238)                                             #click the user

    sleep(1)
    click(x=800, y=657)                                             #click message box

    sleep(1)
    click(x=1127, y=59)                                             #tab to call

def WhatsappVideoCall(name):
    startfile("C:\\Users\\mayan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=201, y=109)                                            #tab to search bar

    sleep(1)
    write(name)

    sleep(1)
    click(x=203, y=238)                                             #click the user

    sleep(1)
    click(x=800, y=657)                                             #click message box

    sleep(1)
    click(x=1079, y=56)                                             #tab to VideoCall    

def WhatsappChat(name):
    startfile("C:\\Users\\mayan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(10)
    click(x=201, y=109)                                            #tab to search bar

    sleep(1)
    write(name)

    sleep(1)
    click(x=203, y=238)                                             #click the user

    sleep(1)
    click(x=800, y=657)                                             #click message box

    sleep(1)
 
#def ZoomMetting():
    #startfile("C:\\Users\\mayan\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    #sleep(20)
    

def CromeAuto(command):
    query = str(command)
    if 'new tab' in query:
        press_and_release('ctrl + t')

    elif 'close tab' in query:
        press_and_release('ctrl + w')

    elif 'new window' in query:
        press_and_release('ctrl + n')    

    elif 'history' in query:
        press_and_release('ctrl + h')    

    elif 'download' in query:
        press_and_release('ctrl + j')    

    elif 'bookmark' in query:
        press_and_release('ctrl + d')  
        press('enter')

    elif 'reopen previous tab' in query:
        press_and_release('Ctrl + SHIFT + t')      

    elif 'home' in query:
        press_and_release('Alt + Home')          

    elif 'close the tab' in query:
        press_and_release('Ctrl + w') 

    elif 'close the window' in query:
        press_and_release('Ctrl + SHIFT + w') 

    elif 'minimize the current window' in query:
        press_and_release('Alt + SPACE + n')     

    elif 'Maximize the current window' in query:
        press_and_release('Alt + SPACE + x')  

    elif 'Reload the current page' in query:
        press_and_release('Ctrl + r')      

    elif 'switch tab' in query:
        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to ", "")
        num = Tab
        sw = f'ctrl + {num}'
        press_and_release(sw)
    
    elif 'open' in query:
        name = query.replace("open ", "")
        NameA = str(name)

        if 'youtube' in NameA:
            speak("open youtube.com")
            web.open("https://www.youtube.com/")

        elif "open stackoverflow" in NameA:
            speak("Here you go to Stack Over flow, Happy coding")
            web.open("https://www.stackoverflow.com/")      

        elif "open google" in NameA:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            web.open(f"{cm}")
            speak("Here search results")    

        elif "open mail" in NameA or "check my mails" in NameA:
            speak("sure sir")
            web.open("https://www.gmail.com/")    

        elif "open facebook" in NameA:
            speak("sure sir, opeaning facebook")
            web.open("https://www.facebook.com/")        

        elif "open instagram" in NameA:
            speak("okay sir, i execute instagram")
            web.open("https://www.instagram.com/")    

        elif "open twitter" in NameA:
            speak("okay sir, open twitter")
            web.open("https://www.twitter.com/")   

        