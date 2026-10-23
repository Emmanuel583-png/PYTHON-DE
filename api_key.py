import requests

u = requests.get("https://jsonplaceholder.typicode.com/users")

j = u.json()

print(j)