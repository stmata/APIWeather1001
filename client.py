import requests

url = "http://127.0.0.1:8008/info"

resp = requests.get(url)
print(resp.json())