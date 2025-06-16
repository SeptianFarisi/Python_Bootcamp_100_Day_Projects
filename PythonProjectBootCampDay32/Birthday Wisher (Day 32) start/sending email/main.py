import smtplib
import datetime as dt
from random import randrange

my_email = "clownjoker310@gmail.com"
password = "coct yngk rlpk smlk"



with open("quotes.txt") as quote:
    quote_list = [q for q in quote]

random = randrange(len(quote_list))
random_quote = quote_list[random]

time = dt.datetime
if time.now().weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Quotes of today\n\n{random_quote}")