import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "6b8f70e448f97b359a7b528d6015c209"
Account_SID = "ACf36f836faab7e061161406ba02f93e7c"
Auth_Token = "c52e3b58e7dbe108347d1ed282e2338e"

weather_params = {
    "lat":20.705540,
    "lon":77.002780,
    "appid":api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hourly_data in weather_data["list"]:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(Account_SID, Auth_Token)
    message = client.messages.create(
                              body='its going to rain today, bring an umbrella',
                              from_='+19143318988',
                              to='+918982198256'
                          )
    print(message.status)
