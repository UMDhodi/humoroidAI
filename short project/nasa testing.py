import requests
import os
import random
import pyttsx3
from PIL import Image

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