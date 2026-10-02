import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true"

try:
    response = requests.get(url, timeout=50)
    if response.status_code == 200:
        data = response.json()
        with open("weather_data.json", "w") as file:
            json.dump(data, file, indent=4)
            print("successful")
    else:
        print(f" Failed: {response.status_code}")
except requests.exceptions.ConnectionError:
    print("Please for the love of God, check your connection!! 🤬")
