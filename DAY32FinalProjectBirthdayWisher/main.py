import smtplib
from datetime import datetime
import pandas
import random


MY_EMAIL = "njnrjpt@gmail.com"
MY_PASSWORD = "banthnnsjzhkntqe"

today = datetime.now()
print(today)
today_1 = (today.month, today.day)
print(today_1)

data = pandas.read_csv("C:\Desktop\Downloads/birthdays.csv")
print(data)
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthdays_dict)

if today_1 in birthdays_dict:
    birth_per = birthdays_dict[today_1]
    print(birth_per)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birth_per["name"])
        print(contents)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        print("login success")
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birth_per["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}".encode("utf8"))
    print(f"Email has been sent to {birth_per['email']}" )


