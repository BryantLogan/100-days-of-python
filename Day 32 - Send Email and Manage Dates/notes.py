from calendar import weekday
import smtplib
import datetime as dt
import random
my_email = "example@example.com"
my_password = "abcd1234"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="bryant.logan1@gmail.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()

# date_of_birth = dt.datetime(year = 1989, month= 3, day= 16)

# print(date_of_birth)

now = dt.datetime.now()
weedkay = now.weekday()

if weekday == 1:
    with open("Day 32 - Send Email and Manage Dates\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )