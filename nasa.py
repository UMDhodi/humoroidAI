import requests
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
import random
import pyttsx3
from PIL import Image
from datetime import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)

def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()

Api_key = "Coo6qmB5pG69bPVapl2wvIJkN3VfwdwfeTNEB7Jg"

def NasaNews(Date):

	speak("Wait sir, i extractingd data from nasa database")
	Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)
	Params = {'date':str(Date)}
	r = requests.get(Url,params = Params)
	Data = r.json()
	Info = Data['explanation']
	Title = Data['title']
	print(Title)
	print(Info)
	Image_Url = Data['url']
	Image_r =requests.get(Image_Url)

	FileName = str(Date) +'.jpg'
	with open(FileName,'wb') as f:
		f.write(Image_r.content)
	Path_1 = "C:\\Users\\mayan\\Desktop\\AI\\" + str(FileName)
	Path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\Nasa Database\\output data\\" + str(FileName)
	os.rename(Path_1, Path_2)
	img = Image.open(Path_2)
	img.show()

	speak(f"Title: {Title}")
	speak(f"According to nasa: {Info}")
	
def DataSummary(Body):
	list__ = ('1','2','3','4','5','6','7','8','9','10')
	value = random.choice(list__)
	path = 'C:\\Users\\mayan\\Desktop\\AI\\Database\\Nasa Database\\Used image\\' + str(value) + ".jpg"
	os.startfile(path)
	name = str(Body)
	url = "https://hubblesite.org/api/v3/glossary/" + str(name)
	r = requests.get(url)
	Data = r.json()
	if len(Data) !=0:
		retur = Data['definition']
		speak(f"According to nasa: {retur}")

	else:
		speak("No Data found at this time! sir please try again later...")

def IssTracker():
	url = "http://api.open-notify.org/iss-now.json"
	r = requests.get(url)
	Data = r.json()
	dt = Data['timestamp']
	lat = Data['iss_position']['latitude']				#Latitude
	lon = Data['iss_position']['longitude']				#Longitude
	speak(f"Time and date: {dt}")
	speak(f"Latitude:{lat}")
	speak(f"Longitude: {lon}")

	plt.figure(figsize=(10,8))
	ax = plt.axes(projection = ccrs.PlateCarree())
	ax.stock_img()
	plt.scatter(float(lon),float(lat),color= 'blue' , marker='o')
	plt.show()

def SolarBodies(body):
	url = "https://api.le-systeme-solaire.net/rest/bodies/"
	r =requests.get(url)
	Data = r.json()
	bodies = Data['bodies']
	Number = len(bodies)

	url_2 = f"https://api.le-systeme-solaire.net/rest/bodies/{body}"
	rrr = requests.get(url_2)
	data_2 = rrr.json()

	mass = data_2['mass']['massValue']
	volume = data_2['vol']['volValue']
	density = data_2['density']
	gravity = data_2['gravity']
	escape = data_2['escape']
	speak(f"Number of bodies in solar system: {Number}")
	speak(f"Mass of {body} is {mass}")
	speak(f"Gravity of {body} is {gravity}")
	speak(f"Escape Velocity of {body} is {escape}")
	speak(f"Density of {body} is {density}")

def Astro(start_date,end_date):
	url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_key}"
	r = requests.get(url)
	Data = r.json()
	Total_Astro = Data['element_count']
	neo =Data['near_earth_objects']
	speak(f"Total astroid between {start_date} and {end_date} is: {Total_Astro}")
	speak("Extact data for astroids are listed below, sir...")

	for body in neo[start_date]:
		id = body['id']
		name = body['name']
		absolute = body['absolute_magnitude_h']
		print(id,name,absolute)
		


	  