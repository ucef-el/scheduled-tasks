import requests
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("PASSWORD")
URL= os.environ.get("URL")


parameters = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": os.environ.get("APPID"),
    "cnt": 4,
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_list = weather_data["list"]

will_be_raining = True

for count in weather_list:
    weather_id = count["weather"][0]["id"]
    if weather_id > 800:
        will_be_raining = True

if will_be_raining:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL,PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg="Subject: Test\n\nBring an Umbrella")
