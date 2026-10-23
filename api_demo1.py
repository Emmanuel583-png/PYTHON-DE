import requests 

url = "https://pokeapi.co/api/v2/ability/7/"

response = requests.get(url)

data = response.json()

print(data.keys())

che = data['id']

print(che)



