import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"we get this status message {response.status.code}")