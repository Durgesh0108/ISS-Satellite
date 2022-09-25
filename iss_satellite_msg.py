import time

import requests
import datetime as dt
import smtplib

MY_LAT = 19.203752
MY_LONG = 72.833230

def iss_is_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameter = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "formatted": 0
    }

    sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    sunrise_sunset_response.raise_for_status()
    data = sunrise_sunset_response.json()

    sunrise = data['results']['sunrise']
    sunset = data['results']['sunset']

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True

while True:
    time.sleep(60)
    if iss_is_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="drgaming143@gmail.com", password="9653320535")
            connection.sendmail(
                from_addr="drgaming143@gmail.com",
                to_addrs="drgaming143@gmail.com",
                msg="Subject:Satellite \n\n Look Up in the Sky the Satellite is Here!!!!")
