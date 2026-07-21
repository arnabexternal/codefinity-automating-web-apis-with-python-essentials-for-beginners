import requests

def fetch_berlin_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    data = response.json()
    temperature = data["current_weather"]["temperature"]
    windspeed = data["current_weather"]["windspeed"]
    print(f"Temperature: {temperature}°C, Wind Speed: {windspeed} m/s")

fetch_berlin_weather()