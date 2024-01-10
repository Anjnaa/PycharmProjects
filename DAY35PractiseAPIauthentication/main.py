import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "6b8f70e448f97b359a7b528d6015c209"
weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid ": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
# print(response.raise_for_status())
print(response.json())
