import pyautogui
import os
import pyttsx3
import time
from PIL import Image

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',160)

def speak(audio):
	engine.say(audio)
	print(audio)
	engine.runAndWait()


#speak("sir, please tell me the name for this screenshot file")
name = ("Test")
#speak("please sir hold the screen for few seconds, i am taking screenshot")
time.sleep(3)
FileName = pyautogui.screenshot()
FileName.save(f"{name}.jpg")
Path_1 = "C:\\Users\\mayan\\Desktop\\AI\\" + str(FileName)
Path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\Screenhots\\"  + str(FileName)
os.rename(Path_1, Path_2)
img = Image.open(Path_2)
img.show()
speak("i  am done sir, the screenshot is saved in your database ... now i  am ready for your next work")