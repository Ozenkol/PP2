from datetime import date

date1 = date(*map(int, input().split()))
date2 = date(*map(int, input().split()))

print(abs(date2-date1).days*24*60*60)
