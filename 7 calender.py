# Write a Python program to display calendar.

import calendar
year, month = int(input('Enter Year :- ')), int(input('Enter month :- '))
cal = calendar.month(year, month)
print(cal)
