import requests
from datetime import datetime
import smtplib
import time




"""301: ISS Overhead notifier project"""

IND_LAT = 20.593683
IND_LONG = 78.962883
sender_email = "njnrjpt@gmail.com"
sender_password = "banthnnsjzhkntqe"
receiver_email = "anjanarajput44@yahoo.com"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])
    iss_position = (iss_lat, iss_long)

    if IND_LAT-5 <= iss_lat <= IND_LAT+5 and IND_LONG-5 <= iss_lat <= IND_LONG+5:
        return True



def is_night():
    parameters = {
        "lat": IND_LAT,
        "long": IND_LONG,
        "formatted": 0
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=sender_email, password=sender_password)
            print("login success")
            connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                                msg=f"Subject:Look UP \n\nThe ISS is above you in the sky".encode("utf8"))
            print("Email has been sent to ", receiver_email)