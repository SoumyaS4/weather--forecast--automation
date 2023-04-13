import requests
from twilio.rest import Client

from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "Your Account Api Key"
account_sid = "Your Account sid"
auth_token = "Your Account Token"
parameters = {
    "lat": 12.9767936,
    "lon": 77.590082,
    "exclude":"current,minutely,daily",
    "appid": API_KEY
}


response = requests.get(OWM_ENDPOINT, params=parameters)
# print(response.status_code)
response.raise_for_status()


data = response.json()
weather_slice = data ["hourly"][:12]



will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        print("bring an umbrella")
        will_rain = True

if will_rain :
    print("bring an umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages\
        .create(
        body="its going to rain today bring an Umbrella!",
        from_='+15165186324',
        to='+919880218868'
    )
    print(message.status)