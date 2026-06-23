import requests

url = "https://www.graduates24.com"

response = requests.get(url)

print(response.status_code)
