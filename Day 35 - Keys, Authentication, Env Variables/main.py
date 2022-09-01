import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

api_key = "API_KEY_HERE"
MY_LAT = 41.765770 # Your latitude
MY_LONG = -72.673363 # Your longitude
account_sid = "AC82f11b4d12376af5d0ab7cc210164278"
auth_token = "AUTH_TOKEN_HERE"

proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
hourly_slice = data["hourly"][:12]

will_rain = True

for hour_data in hourly_slice:
    condition_num = hour_data["weather"][0]["id"]
    if int(condition_num) < 700:
        will_rain = False

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Bring an umbrella",
        from_='+16064411948',
        to='+5855034132'
    )
    print(message.status)
        