import requests

url = 'http://127.0.0.1:8000/v1/upload'
files = {'file': open('manifiesto_ok.csv', 'rb')}

r = requests.put(url, files=files)

print(r)