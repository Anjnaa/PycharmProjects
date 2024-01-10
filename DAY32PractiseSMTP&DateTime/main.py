
import smtplib
import datetime as dt
import random

sender_email = "njnrjpt@gmail.com"
sender_password = "banthnnsjzhkntqe"
receiver_email = "anjanarajput44@yahoo.com"

now = dt.datetime.now()
print(now)
day = now.weekday()
print(day)

if day == 5:
    with open(file="quotes.txt", encoding="utf8") as quotes:
        quotes_file = quotes.readlines()
        quote = random.choice(quotes_file)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        print("login success")
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
                            msg=f"Subject: Today's Motivation \n\n{quote}".encode("utf8"))
        print("Email has been sent to ", receiver_email)


# message_to_send = ""
#
# with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=sender_email, password=sender_password)
#     print("login success")
#     connection.sendmail(from_addr=sender_email, to_addrs=receiver_email,
#                         msg="Subject: Learning Python \n\nHello Anjana this msg is sent using python.")
#     print("Email has been sent to ", receiver_email)
#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.weekday()
# print(now)
#
# date_of_birth = dt.date(year=1998, month=3, day=11)
# print(date_of_birth)

"""297: API endpoints and making API calls"""

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# if response.status_code != 200:
#     raise Exception("BAD response from ISS API")
#
# if response.status_code == 404:
#     raise Exception("that resource does not exist")
# elif response.status_code == 401:
#     raise Exception("you are not authorised to access this data")

"""298:requests module: errors and exceptions """

# response.raise_for_status()
# data = response.json()
#
# longitude = float(data["iss_position"]["longitude"])
# latitude = float(data["iss_position"]["latitude"])
# iss_position = (latitude, longitude)
# print(iss_position)


"""300:API Parameters"""
#
# IND_LAT = 20.593683
# IND_LONG = 78.962883
#
# parameters = {
#     "lat": IND_LAT,
#     "long": IND_LONG,
#     "formatted": 0
# }
#
# response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# print(data)
#
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
# print(sunrise)
# print(sunset)
# print(sunrise.split("T")[1].split(":")[0])
# print(sunset.split("T")[1].split(":")[0])
# time_now = datetime.now()
# print(time_now.hour)

