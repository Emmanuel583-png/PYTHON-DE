import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true"
try:
    response = requests.get(url, timeout=15)

    if response.status_code == 200:
        data = response.json()
        weather = data['current_weather']
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Windspeed: {weather['windspeed']}km/h")
    else:
        print(f"Failed: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("no internet connection")

except requests.exceptions.Timeout:
    print("request timed out")