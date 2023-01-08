from bs4 import BeautifulSoup as Bs
import requests

def get_price(url):
    data = requests.get(url)
    soup = Bs(data.text ,'html.parser')
    ans = soup.find("div", class_ = "BNeawe s3v9rd AP7Wnd") .text
    return ans

url = "https://www.google.com/search?q=gold+price"    
ans = get_price(url)
print (ans)