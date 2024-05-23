import os
import requests
from twilio.rest import Client

#API connection
url= "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("XXXX")
weather_params = {
    "lat": 25.286106,
    "lon": 51.534817,
    "appid":api_key,
    "cnt": 4,
}

#Fetching data from the url
response = requests.get(url, params=weather_params)
response.raise_for_status()
weather_data = response.json() #convert the data into json format

#Twilio authorisation keys
account_sid = "XXXXX"
auth_token = os.environ.get("XXX")

#analysing the data
is_raining = False
for rain in weather_data["list"]:
    weather_condition = rain["weather"][0]["id"]
    if int(weather_condition)< 700:
        is_raining = True

#Sending message through Twilio
if is_raining:
    
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Its going to rain today",
            from_= "XXXXX",
            to= "XXXXX"
        )
    
    print(message.status)

