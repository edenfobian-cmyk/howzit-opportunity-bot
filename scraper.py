import requests

url = "https://www.graduates24.com"

response = requests.get(url)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("Saved page")
