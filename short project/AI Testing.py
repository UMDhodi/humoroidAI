import instaloader
import webbrowser as web
import time
import shutil
import glob
from os import path

print("okay sir, please enter the username")
name = input("Enter username here:")
web.open(f"www.instagram.com/{name}")
print(f"sir, here is the profile of the user {name}")
time.sleep(5)
mod = instaloader.Instaloader()
mod.download_profile(name, profile_pic_only=True)   

file_path_1 = "C:\\Users\\mayan\\Desktop\\AI\\" +str(name)
file_path_2 = "C:\\Users\\mayan\\Desktop\\AI\\Database\\Instaloader Database"
shutil.move(file_path_1, file_path_2)
print("Done sir, profile picture is saved in our main folder....")
                
