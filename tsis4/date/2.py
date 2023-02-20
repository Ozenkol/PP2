from datetime import date
from datetime import timedelta

today = date.today()
tomorrow = today + timedelta(1)
yesterday = today - timedelta(1)

print(yesterday, today, tomorrow, sep='\n')
