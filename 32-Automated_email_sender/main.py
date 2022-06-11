# ---------------------- Send email using python -------------------------
# import smtplib

# my_email = "dummy@gmail.com"
# password = "dummye1212()"

# with smtplib.SMTP('smtp.gmail.com') as connection:
#   connection.starttls()
#   connection.login(user=my_email, password=password)
#   connection.sendmail(from_addr= my_email, to_addrs='demail67@yahoo.com', msg='Subject:hello\n\nThis is the content')

# ---------------------- Python Date Time Module -------------------------

# import datetime as dt

# current_date_time = dt.datetime.now()
# date = current_date_time.date()
# time = current_date_time.time()
# print(date)
# print(time)

# ---------------------- Challenge 1 -------------------------

import smtplib
import datetime as dt
import random

MY_EMAIL = "put here your email"
MY_PASSWORD = 'your password'

now = dt.datetime.now()
week = now.weekday()
if week == 1:
  with open('quotes.txt') as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)
  
  with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs='tahawarihsan@gmail.com', msg=f'Subject:Teri ukat to nai itni heavy quote lkn phr b aysh kr\n\n{quote}')
