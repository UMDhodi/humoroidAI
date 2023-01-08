from cv2 import data
import requests
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)

def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()

def Geo():

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

