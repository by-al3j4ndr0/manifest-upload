import requests

url = 'https://alejandroperezhdez.pythonanywhere.com/v1/query'
params = {'hbl': 'GDT24356714'}

r = requests.get(url=url, params=params)

print(r)

API_DATA  = r.json()
print(API_DATA)

for key in API_DATA:
    print(key, ":", API_DATA[key])