import requests
import json

url = "https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true"

try:
    response = requests.get(url, timeout=50)
    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        print(f"Temperature: {weather['temperature']}°c")
        print(f"windspeed: {weather['windspeed']}km/h")
        with open("weather.json", "w") as file:
            json.dump(weather, file, indent=4)
    else:
        print(f"failed: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("no internet connection")

except requests.exceptions.Timeout:
    print("request timed out")
