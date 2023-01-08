import imdb
import requests

ia = imdb.IMDb()
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
print(url)

				

