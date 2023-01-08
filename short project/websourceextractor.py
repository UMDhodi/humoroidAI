from urllib.request import urlopen

open_url = urlopen('https://www.instagram.com/')
webcontent = open_url.read()
print(webcontent)