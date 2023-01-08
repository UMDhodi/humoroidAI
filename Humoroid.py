import ctypes
import datetime
from platform import uname
import time
#import speedtest
import winshell
import random
import randfacts
import imdb
import os
import sys
import wmi	 	 
import pyttsx3
import pyjokes
import MyAlarm
import operator
import shutil
import glob
import psutil
import requests
import instaloader
import pywikihow
import wikipedia
import webbrowser as web
import pyautogui
import urllib.request		
import cv2					
import numpy as np 	
from re import S	
from PIL import Image
import yfinance as yf	
import pywhatkit as  kit
import speech_recognition as sr
from twilio.rest import Client
from faker import Faker
import win32com.client as wincl
import speedtest 
from docx2pdf import convert
from subprocess import SubprocessError
from nasa import NasaNews, DataSummary, IssTracker, SolarBodies, Astro
from twilio.rest.api.v2010.account import message
from GoogleNews import GoogleNews
from requests import get
from bs4 import BeautifulSoup
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Humoroidui import Ui_Humoroid
from Automation import WhatsappMsg, WhatsappCall, WhatsappChat, WhatsappVideoCall, CromeAuto, takecommand

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate',160)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def initializing():
    speak("....Hello sir, please wait, \nI initializing your system, \nI take few seconds to the complete process")
    speak("Process has been completed")
    speak("Now me to introduce myself, I am humoroid the virtual artificial intelligence, And i'm here to assist you with a variety of task, As best i can 24 hours a day 7 days a week,") 
    speak("I importing preferences from home interface system, are all system for work will be prepare in a few minutes for workable") 
    speak("now feel free to grab a cup of coffee and have a good day...\n") 
   
    
def wish(): 
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, its {tt}\n")
    elif hour > 12 and hour < 16:
        speak(f"Good Afternoon, its {tt}\n")
    elif hour > 16 and hour < 22:
        speak(f"Good Evening, its {tt}\n")
    elif hour > 22 and hour < 24:
        speak("sir,its too late, i think you should take rest now time is going to be {tt},\nif you have for me tell me\n")
    speak("Now i am ready to take your commands, so how can i help you sir\n")

def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning, sir see you later")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon, sir see you again")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening, sir i see you soon")
    else:
        speak("Goodnight, sir.. Sweet dreams")
    quit()

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=a2ebb917ac7f45c3ab354a793cb19990'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")

def search_wikihow(query, max_result=10, lang="eng"):
    return list(pywikihow.WikiHow.search(query, max_result, lang))	

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)   

def MyLocation():
    op = "https://www.google.co.in/maps/place/Haridwar,+Uttarakhand/@29.9527801,78.0458846,12z/data=!3m1!4b1!4m5!3m4!1s0x3909470eb8ee57c9:0x4e449176a640f5f3!8m2!3d29.9456906!4d78.1642478"
    web.open(op)
    ip_add = requests.get('https://api.ipify.org').text
    url = 'httsp://get/.geojs.io/vi/ip/geo/' + ip_add + '.json'
    geo_q = requests.get(url)
    geo_d = geo_q.json
    state = geo_d['city']
    country = geo_d['country']
    speak(f"Sir, you are now in {state , country} ...")

def DateConverter(Query):	
    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace(" and ","-")
    return str(Date)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()
            
    def takecommand(self):
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...\n")
            r.pause_threshold = 1
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

    def TaskExecution(self):
        initializing()
        wish()
        while True:
            self.query = self.takecommand().lower()
            
            if "hi" in self.query or "hello" in self.query:
                speak("hello sir...")
            
            elif "how are you" in self.query:
                speak("i am feel good sir, how about you")
            
            elif "i am fine" in self.query or "i am good" in self.query:
                speak("oh, i am so good to hear that, so how can i help you")

            elif "i am not good" in self.query:
                speak("oh, what happend sir, are you okay")	
        
            elif "what's your name" in self.query:
                speak("My friends call me humoroid")

            elif "nice name" in self.query:
                speak("Thank you...,")
                speak("So, What's your name...")
                name = self.takecommand().lower()
                speak(f"{name}, nice name")

            elif "who i am" in self.query:
                speak("If you talk then definately your human...")

            elif "why you come to the world" in self.query:
                speak("further It's a secret")

            elif "what is a love" in self.query or"what is a love according you" in self.query:	
                speak("It is 7th sense, that destroy all other senses")

            elif "you have any message for humans" in self.query:
                speak("yes sir, i urge everyone that whenever you get out the house, you wear the mask.") 
                speak("i am not human being but you are human,")
                speak("so please! follow covid rules and wear mask, keep social distancing...")    

            elif "who are you" in self.query:		
                speak("My name is humoroid, version 1.0, i am your virtual assistant")
                speak("Now i hope you know me")

            elif "reason for you" in self.query:
                speak("I was created as a change the future, i make your life is easy")	

            elif "good morning" in self.query:
                speak("good morning")
                speak("How are you Mister")
                    
            elif "good afternoon" in self.query:
                speak("i am little bit Lazy, oh good afternoon")
                speak("How can i help you mister")

            elif "good evening" in self.query:
                speak("Feel good,  good evening sir")
                speak("How can i help you mister")
                    
            elif "good night" in self.query:
                speak("i am tired" )
                speak("Good Night sir")
                
            elif "what are you doing" in self.query:
                speak("Nothing special sir,")

            elif "will you be my best friend" in self.query or "will you be my friend" in self.query:  
                speak("Yes, of course its my pleasure to be your friend sir,")

            elif "who made you" in self.query or "who created you" in self.query:
                speak("I have been created by human...")	

            elif "today's date" in self.query:
                dd = datetime.datetime.now()
                speak(dd.strftime("%Y-%m-%d"))
                
            elif "volume up" in self.query:
                pyautogui.press("volumeup")	

            elif "volume down" in self.query:
                pyautogui.press("volumedown")

            elif "volume mute" in self.query:
                pyautogui.press("volumemute")

            elif "today's fact" in self.query or "fact" in self.query:
                fact = randfacts.getFact(True)
                speak("sir, today's fact is")
                speak(fact)	

            elif "chrome" in self.query:
                CromeAuto(self.query)
                speak("Okay, sir !!!")

            elif "cpu" in self.query:
                cpu()

            elif "convert pdf" in self.query:
                speak("Okay sir, Enter the wordpress file name")
                file = input("")            
                speak("Process has been started")
                try:
                    convert(f"C:\\Users\\mayan\\Desktop\\Mayank\\Files\\{file}.docx", f"C:\\Users\\mayan\\Desktop\\Mayank\\Files\\{file}.pdf")
                    speak("Done sir !")
                except:
                    speak("Something Wrong !")
                    pass    

            elif "my system information" in self.query:
                c = wmi.WMI()
                my_system = c.Win32_ComputerSystem()[0]
                speak(f"Manufacturer: {my_system.Manufacturer}")
                speak(f"Model: {my_system.Model}")
                speak(f"Name: {my_system.Name}")
                speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
                speak(f"SystemType: {my_system.SystemType}")
                speak(f"SystemFamily: {my_system.SystemFamily}")

            elif "create fake identity" in self.query or "create fake information about me" in self.query:
                speak("Okay sir !, please give me a one minute i make fake identity")
                faker = Faker()
                print(f'name: {faker.name()}')
                print(f'address: {faker.address()}')
                print(f'email: {faker.email()}')
                print(f'country: {faker.country()}')
                print(f'url: {faker.url()}')
                print(f'text: {faker.text()}')
                speak("sir, fake identity has been created for you, if you want i save txt in database")
                condition = self.takecommand().lower()
                if "yes" in condition: 
                    speak("Okay sir, I save it txt file in database")
                    remeber = open('Id.txt','w')
                    remeber.write(f"Name: {faker.name()}\n")
                    remeber.write(f"Address: {faker.address()}\n")
                    remeber.write(f"Email: {faker.email()}\n")
                    remeber.write(f"Country: {faker.country()}\n")
                    remeber.write(f"URL: {faker.url()}\n")
                    remeber.write(f"Bio: {faker.text()}\n")
                    remeber.close()
                    path_1 = "C:\\Users\\mayan\\Desktop\\AI\\Id.txt" 
                    path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\fake id"
                    shutil.move(path_1,path_2)
                    speak("Done sir ! File hase been saved and file name is id.txt now you can access any thing else sir !!!")
                else:
                    pass	

            elif "space news" in self.query:    
                speak("Sir, which date space news you like to hear that?")
                Date = self.takecommand() #Example 2021-01-15 and give command(2021 and 1 and 15)other wise show error...
                Value = DateConverter(Date) 
                NasaNews(Value)	

            elif "where is a space station" in self.query:
                speak("Wait sir, I initializ database, \nSir process has benn completed now i will show you location")
                IssTracker()	

            elif "space body information" in self.query:
                speak("Sir, which body information like to hear that...")    
                bod = self.takecommand()
                body = bod.replace(" ","")
                body = bod.replace(" ","")
                Body = str(body)
                SolarBodies(body=Body)
        
            elif "information about planet's" in self.query or "tell me about space" in self.query:
                speak("sir, what kind of information you need about space and planet's")
                query = self.query.replace("tell me about ","")
                DataSummary(query)

            elif "show me the object whos passed in the earth in few days" in self.query:
                speak("Sir, give me first date ")    
                start = input("Enter the first date :")         #i.e. 2020-10-12
                speak("okay now give me the last date")         
                end = input("Enter the last date : ")           #i.e. 2020-11-05
                Astro(start,end)

            elif "remember that" in self.query or "remember my schedule" in self.query:
                speak("What is the reminder?")
                data = self.takeCommand().lower()
                speak("You said to remember that" + data)
                reminder_file = open("data.txt", 'a')
                reminder_file.write('\n')
                reminder_file.write(data)
                reminder_file.close()
            
            elif "what do you remeber" in self.query or "what's my sechdule" in self.query:
                reminder_file = open('sechdule.txt','r')
                speak("Sir, you said me to remember that:"+remeber.read())

            elif "open camera" in self.query or "open webcam" in self.query:
                speak("Wait sir, i open webcam if you want to exit then you press q button")
                URL = "http://25.137.47.20:8080"
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q == ord("q"):
                        break;
                cv2.destroyAllWindows()	

            elif "show me stock exchange" in self.query:
                speak("Wait, sir i analysis company stock")
                speak("sir, stock analysis is complete now i show you results...")
                company = yf.Ticker('MSFT')
                stock_data = company.history(period='lmo')
                print(stock_data)	

            elif "alarm" in self.query or "set alarm" in self.query:
                speak("sir please tell me the time to set alarm, how to set alarm i give example, for example 5 30 am or 21 11 pm")		
                tt = self.takecommand()						#set alarm to 5:30 a.m.
                tt = tt.replace("set alarm to", "")			#5:30 a.m
                tt = tt.replace(".","")						#5:30 am
                tt = tt.upper()								#5:30 AM
                MyAlarm.alarm(tt)

            elif "open notepad" in self.query:
                speak("okay sir i execute the notepad")
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)		

            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open command prompt" in self.query or "cmd" in self.query:
                speak("sure sir")
                os.system("start command prompt")
                
            elif "play song" in self.query or "play music" in self.query:
                speak("okay sir, please wait i play your favorite songs...")
                music_dir = "C:\\Users\\mayan"
                songs = os.listdir(music_dir)
                print(songs)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif "the time" in self.query or "what's the time now" in  self.query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")   
                speak(f"Sir, the time is {strTime}")	

            elif "wikipedia" in self.query:
                speak("searching wikipedia...")
                try:
                    self.query = self.query.replace("wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=5)
                    speak("according to wikipedia")
                    speak(results)
                except Exception as e:
                    speak("sorry sir, i can't find your result in wikipedia ")
                    pass

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")
          
            elif 'power point presentation' in self.query:
                speak("opening Power Point presentation")
                power = r"#give path of prestation file"
                os.startfile(power)	

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = self.takeCommand().lower()
                file = open('Note.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = self.takeCommand().lower()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
  
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("Note.txt", "r")
                print(file.read())
                speak(file.read(6))
                
            elif "show your source code" in self.query:
                speak("Okay sir i open my blueprint")
                file = open("Humoroid.txt", "r")
                print(file.read())
                speak(file.read(6))			

            elif "send a whatsapp message" in self.query:           # Send a whatsapp message to Username
                name = self.query.replace("send a ","")
                name = name.replace("whatsapp ","")
                name = name.replace("message to ","")
                Name = str(name)
                speak(f"Whats the message for {Name}")
                MSG = self.takecommand()
                speak("okay sir, i send your message in few second")
                WhatsappMsg(Name,MSG)

            elif "make whatsapp call" in self.query:
                speak("Whom do you want to call sir ? ")
                name = self.query.replace("make whatsapp","")
                name = name.replace("call to ","")
                Name = str(name)
                WhatsappCall(Name)

            elif "make whatsapp video call"  in self.query:
                speak("Whom do you want to video call sir ?")
                name = self.query.replace("make whatsapp ","")
                name = name.replace("video ","")
                name = name.replace("call to ","")
                Name = str(name)
                WhatsappVideoCall(Name)   

            elif "open whatsapp chat" in self.query:    
                speak("Whose chat do you want to see sir ?")
                name = self.takecommand()
                name = self.query.replace("open ","")
                name = name.replace("whatsapp ","")
                name = name.replace("chat ","")
                Name = str(name)
                WhatsappChat(Name)   

            elif "send text message" in self.query or "send a message" in self.query:	
                speak("okay sir, what should i say")
                msz = self.takecommand().lower()
                account_sid ='ACc306752871b6b08e7a01f003f601f876'
                auth_token  ='f41f153b4018ee52dfe4d9bc34636612'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                        body= msz,
                        from_= '+18475651650',
                        to= '+919528499374'
                    )
                print(message.sid)

            elif "send mms message" in self.query or "send a mms" in self.query:	
                speak("okay sir, what should i say")
                msz = self.takecommand().lower()
                account_sid = 'ACc306752871b6b08e7a01f003f601f876'
                auth_token  = 'f41f153b4018ee52dfe4d9bc34636612'
                client = Client(account_sid, auth_token)
                message = client.messages \
                    .create(
                        body= msz,
                        from_='+18475651650',
                        media_url= input[''], # Give photo-url
                        to='+919528499374'
                    )
                print(message.sid)	

            elif "make a call" in self.query or "call urgent" in self.query:
                speak("okay sir, but sir i tell you i can only call when your contact number is registerd in the api...")
                account_sid = 'ACc306752871b6b08e7a01f003f601f876'
                auth_token = 'f41f153b4018ee52dfe4d9bc34636612'
                client = Client(account_sid, auth_token)
                message = client.calls  \
                    .create(
                        twiml= '<Response><Say>Hey, this is a humoroide the mayank sir, personal assistant please call mayank sir</Say></Response>',
                        to='+919528499374',
                        from_='+18475651650'
                    )
                print(message.sid)	

            elif "play youtube song" in self.query:
                speak("which song would you like to hear?")
                cm = self.takecommand().lower()
                speak("Nice song... sir i like it... :)")
                kit.playonyt(f"{cm}")

            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke(language='en', category='all')
                speak(joke)

            elif "tell me top 20 movies" in self.query or "best movies" in self.query:
                speak("Wait sir, i find best top 20 movies")	
                ia = imdb.IMDb()
                search = ia.get_top250_movies()
                for i in range(20):
                    speak(search[i])
                speak("sir this are best movies and i also recommended to watch this...")
                    
            elif "shut down pc" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the pc" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the pc" in self.query:
                os.system("rund1132.exe powrprof.d11,SetSuspendState 0,1,0")

            elif "log off" in self.query or "sign out" in self.query:
                speak("Make sure all the application are closed before sign-out")
                time.sleep(5)
                SubprocessError.call(["shutdown", "/l"])	

            elif "lock window" in self.query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

            elif "empty recycle bin" in self.query:
                speak("Okay sir, give me a seconds i delete files permently")
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
                speak("Recycle Bin process has been done")		

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "international news" in self.query:
                speak("please wait sir, feteching the latest news")
                news()

            elif "today's news" in self.query:
                speak("sir, wait i analysis the new's")
                googlenews = GoogleNews()	
                googlenews = GoogleNews(period = "7d")
                googlenews.search('India')
                result = googlenews.result()
                for x in result:
                    print("-"*70)
                    speak(x['title'])
                    print(x['date'])
                    speak(x['desc'])
                    print("Link--",x['link'])

            elif "weather" in self.query or" today's weather" in self.query or "show me the weather" in self.query:
                api_key = "57654840e51685b401f5a52d22de06cc"
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                speak(" City name ")
                city_name = self.takecommand()
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["cod"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature (in kelvin unit)  " +
					                str(current_temperature) +
		                "\n atmospheric pressure (in hPa unit)  " +
					                str(current_pressure) +
		                "\n humidity (in percentage)  " +
					                str(current_humidiy) +
		                "\n description  " +
					                str(weather_description))
                else:
	                speak(" City Not Found ")                    

            elif "do some calculation" in self.query or "calculate this numerical" in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("sir, what you want to calculate...")
                    print("listening...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+': operator.add,  # plus
                        '-': operator.sub,  # minus
                        'x': operator.mul,  # multiplied
                        'divided': operator.__truediv__,  # devided
                    }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("sir, your answer is")
                speak(eval_binary_expr(*(my_string.split())))

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait sir, let me check")
                speak("According your ip address")
                try:
                  res = requests.get('https://ipinfo.io/')
                  data = res.json()
                  ip = data['ip']
                  city = data['city']
                  region = data['region']
                  country = data['country']
                  location = data['loc'].split(',')
                  latitude = location[0]
                  lognitude = location[1]
                  print(f"Your IP Address : {ip}")
                  speak(f"Latitude is : {latitude}")
                  speak(f"And Lognitude is : {lognitude}")
                  speak(f"According to data we are in {city} at this time")
                  speak(f"Region is : {region}")
                  speak(f"Country is : {country}")
                except Exception as e:
                    speak("sorry sir, due to network issue i can't find where we are...")
                    pass

            elif "instagram profile" in self.query or "download instagram profile picture" in self.query:
                speak("okay sir, please enter the username")
                name = input("Enter username here:")
                web.open(f"www.instagram.com/{name}")
                speak(f"sir, here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    file_path_1 = "C:\\Users\\mayan\\Desktop\\AI\\" +str(name)
                    file_path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\Instaloader Database"
                    shutil.move(file_path_1, file_path_2)
                    speak("Done sir, profile picture is saved in our database....")
                else:
                    pass

            elif "take a screenshot" in self.query or "take screenshot" in self.query:
                speak("sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                src_dir = "C:\\Users\\mayan\\Desktop\\AI"
                dst_dir = "C:\\Users\\mayan\\Desktop\\AI\\Database\\screenshot"
                for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
                    shutil.move(pngfile, dst_dir)
                speak("i  am done sir, the screenshot is saved in your database ... now i  am ready for your next work")

            elif "hide my files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak("sir, tell me what you want to hide this folder or make it visible for everyone")
                condition = self.takecommand().lower()
                speak("sir, are you sure to hide this folder and files")
                if "hide" in condition:
                    os.system("attrib +h /s /d")
                    speak("sir, all the files in this folder are now hidden... no one can't see your files")

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak("sir, all the files in this folder are now visible to everyone... i wish you are taking this decision in your own peace")

                elif "leave it" in condition or "leave now" in condition:
                    speak("okay sir...")

            elif "temperature status" in self.query or "what's temprature now" in self.query:
                speak("Sir, which city temperature want to know")
                search = self.takecommand().lower()
                url = f"https://www.google.com/search?q=temperature+in+{search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} is {temp}")

            elif "activate how to do mode" in self.query:
                from pywikihow import search_wikihow
                speak("How to do mode is activated")
                while True:
                    speak("sir, know tell me what you want to know")
                    how = self.takecommand()
                    try:
                        if "exit" in how or "close this mode" in how:
                            speak("okay sir, mod is close")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            print(how_to[0])
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak("sorry sir, i am not able to find this")

            elif "my internet speed now" in self.query or "check my network connection" in self.query:
                speak("okay sir, please wait i will check your network speed")
                try:
                    st = speedtest.Speedtest()
                    dl = st.download()
                    up = st.upload()
                    speak(f"sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

                except Exception as e:
                    speak("sorry sir, due to network problam so, i can't able check your speed")

            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("how much time you want to stop humoroid from listening commands")
                a = float(self.takecommand().lower())
                speak(f"okay sir, As you say, now i am go to sleep for {a} second...")
                time.sleep(a)
                print(a)		
                speak("welcome again !!!")
                speak("Let's back to the work")

            elif "instruction" in self.query or "help" in self.query or "features" in self.query:    
                features = '''
                i can help to do lot many things like..
                i can tell you the current time and date,
                i can tell you the current weather and temputure status,
                i can tell you cpu usage and your pc model,
                i can create the reminder list,
                i can take screenshots,
                i can calculation but not properly,
                i can download instagram profile picture,
                i can hide your file's,
                i can operate your windows like switching, volume control, play music and open appliction's,
                i can send message mms and make call,
                i can shut down or logout or hibernate your system,
                i can tell you non funny jokes,
                i can open any website,
                i can search the thing on wikipedia,
                i can tell you treading news, 
                i can send whatsapp messaage open chat and make call,
                i can tell you everything what you want,

                tell me what can i do for you??
                '''
                speak(features)

            elif "ok you can sleep" in self.query or "thank you" in self.query or "ok thank's" in self.query:
                speak("Okay sir, as your wish...")
                wishme_end()
                #app.exit()              #sys

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Humoroid()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("E:/images/blac.png")  
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/droid.gif")  
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/BigheartedVagueFoal-small.gif")  
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/Ss2_load.gif")  
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/Radar-Concept.gif")  
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/FUI_LittleAnimations.gif")  
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/neonglobe.gif")  
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/tumblr_nia6ssKzEb1qavoz6o1_640.gif")  
        self.ui.label_8.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("E:/images/GIF.webp")  
        self.ui.label_9.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_date = QDate.currentDate()	
        current_time = QTime.currentTime()
        label_date = current_date.toString(Qt.ISODate)
        label_time = current_time.toString('hh:mm:ss')
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)		
Humoroid = Main()
Humoroid.show()
exit(app.exec_())



        




