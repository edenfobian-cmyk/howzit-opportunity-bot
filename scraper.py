import requests
from bs4 import BeautifulSoup

url = "https://www.graduates24.com/youth_opportunities"

response = requests.get(url)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser")

print("Title:")
print(soup.title.text)
