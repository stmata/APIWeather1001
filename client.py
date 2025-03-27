import requests

url = "https://apiweatherrcw1.azurewebsites.net/info"

resp = requests.get(url)
print(resp.json())