import requests
import datetime as dt
import smtplib


MY_LAT = 19.203752
MY_LONG = 72.833230
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
#
# # to get status Code of the url
# # print(response.status_code)
#
# # print(response)
#
#
# # to get why the error was raised
# # print(response.raise_for_status())
#
#
#
data = iss_response.json()
# print(data)
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])
#
iss_position = (iss_latitude,iss_longitude)
# print(iss_position)
#
# if iss_position == MY_LOCATION:
#     print("its Up there")

parameter = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "formatted":0
}

sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json",params=parameter)
sunrise_sunset_response.raise_for_status()
data = sunrise_sunset_response.json()
# print(data)

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

# to get the hour and minutes of sunrise and sunset
sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
# sunrise_min = int(sunrise.split("T")[1].split(":")[1])
sunset_hour = int(sunset.split("T")[1].split(":")[0])
# sunset_min = int(sunset.split("T")[1].split(":")[1])
print(sunset_hour)

now = dt.datetime.now()

if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
    if now.hour > sunset_hour:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="drgaming143@gmail.com",password="9653320535")
            connection.sendmail(
                from_addr="drgaming143@gmail.com",
                to_addrs="drgaming143@gmail.com",
                msg="Subject:Satellite \n\n Look Up in the Sky the Satellite is Here!!!!")

