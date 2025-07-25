##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

from smtplib import SMTP
from random import randrange
import pandas as pd
from datetime import datetime as dt

my_email = "clownjoker310@gmail.com"
password = "coct yngk rlpk smlk"

file = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month,row.day):row for (index, row) in file.iterrows()}

now = dt.now()
month = now.month
day = now.day
birthday = (month,day)

random = randrange(3) + 1

if birthday in birthdays_dict:
    name = birthdays_dict[birthday]["name"]
    email = birthdays_dict[birthday]["email"]

    with open(f"letter_templates/letter_{random}.txt") as file:
        letter = file.read()
        msg = letter.replace("[NAME]", f"{name}")
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(my_email,email,msg=f"Subject:Happy Birthday!\n\n{msg}")