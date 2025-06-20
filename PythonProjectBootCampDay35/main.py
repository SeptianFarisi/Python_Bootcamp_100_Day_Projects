import requests
import os
from twilio.rest import Client

api_key = os.environ.get("API_KEY")
MY_LAT = -6.175110 # Your latitude
MY_LONG = 106.865036 # Your longitude

param = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4
}
response = requests.get("https://api.openweathermap.org/data/2.5/forecast",params=param)
response.raise_for_status()
data = response.json()
it_rain = False
weather_data = [data["list"][n]["weather"][0]["id"] for n in range(len(data["list"]))]
for i in weather_data:
    if i < 700:
        it_rain = True
if it_rain:
    account_sid = 'ACc9acd5dabefac6e974434619ef9f5f14'
    auth_token = os.environ.get("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Bring an Umbrella',
        to='whatsapp:+6289513989797'
    )

    print(message.sid)