import requests
from bs4 import BeautifulSoup

url = "https://www.graduates24.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify()[:5000])
