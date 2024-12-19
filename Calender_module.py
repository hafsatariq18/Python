# You are given a date. Your task is to find what the day is on that date.

import calendar

X = input().split( )
month = int(X[0])
date = int(X[1])
year = int(X[2])


weekday_index = calendar.weekday(year, month, date)


day_name = calendar.day_name[weekday_index]


print(day_name.upper())