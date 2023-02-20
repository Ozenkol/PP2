import datetime
from datetime import date
from datetime import timedelta

current_date = date.today()

before_date = current_date - timedelta(5)

print(before_date)
