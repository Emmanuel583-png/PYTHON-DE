import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=6.5244&longitude=3.3792&current_weather=true"
response = requests.get(url)

if response.status_code==200:
    data = response.json()
    weather = data['current_weather']
    print(f"Temperature: {weather['temperature']}°c")
    print(f"wind_speed: {weather['windspeed']}km/h")
else:
    (f"maybe this is your issue: {response.status_code}")
