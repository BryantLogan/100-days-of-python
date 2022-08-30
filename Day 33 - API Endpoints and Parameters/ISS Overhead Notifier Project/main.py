import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.765770 # Your latitude
MY_LONG = -72.673363 # Your longitude

my_email = "youremail@email.com" # Your email address
my_password = "password" # Your password

# Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True

# Checking whether it is currently after sunset and before sunrise
def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset and time_now <= sunrise:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

while True:
    time.sleep(60)
    if is_close() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Look Up!\n\nThe ISS Space Station is above you!"
            )
# Added this else block to make sure emails could be sent
    # else:
    #     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    #         connection.starttls()
    #         connection.login(my_email, my_password)
    #         connection.sendmail(
    #             from_addr=my_email,
    #             to_addrs=my_email,
    #             msg=f"Subject:Don't look Up!\n\nThe ISS Space Station is  NOT above you!"
    #         )