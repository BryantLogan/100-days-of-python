from datetime import datetime
import smtplib
import pandas
import random

#Enter your email credentials here, and make sure your email provider allows outside app access

my_email = "example@example.com"
my_password = "abcd1234"

# 1. Update the birthdays.csv with your friends & family's details. 
today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("Day 32 - Send Email and Manage Dates\\birthdays.csv") 

bday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    file_path = f"Day 32 - Send Email and Manage Dates\letter_templates\letter_{random.randint(1,3)}.txt"
    with open (file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=bday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )