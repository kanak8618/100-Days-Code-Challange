import time
from datetime import datetime

#Print current date and time in Python
print(datetime.datetime.now())
print(datetime.datetime.now().time())

# Calculate number of days between two given dates
date_1 = datetime(2020, 2, 25).date()
date_2 = datetime(2020, 9, 17).date()
delta=None
if date_1>date_2:
    delta=date_1-date_2 
else:
    delta=date_2-date_1
 
print("Difference of the days will be: \n",delta.days)

# Convert the following datetime into a string
given_date = datetime(2020, 2, 25)
string_date=given_date.strftime("%Y-%m-%d %H:%M:%S")
string_date

# Print current time in milliseconds
milliseconds=int(round(time.time()*1000))
print(milliseconds)

# Add a week (7 days) and 12 hours to a given date
given_date = datetime(2020, 3, 22, 10, 0, 0)
days_to_add=7
res_date=given_date+timedelta(days_to_add,12)
print("new date will be: \n",res_date)

#Find the day of the week of a given date
given_date = datetime(2020, 7, 26)
given_date.strftime("%A")

# Print a date in a the following format

given_date = datetime(2020, 2, 25)
given_date.strftime("%A %d %b %Y")

#Subtract a week (7 days) from a given date in Python
given_date = datetime(2020, 2, 25)
from datetime import datetime ,timedelta
print(given_date)
days_to_substract=7
res_date=given_date-timedelta(days_to_substract)
print(res_date)

#  Convert string into a datetime object
date_string="Feb 25 2020 4:20PM"
date_time_obj=datetime.strptime(date_string,"%b %d %Y %H:%M%p")
print(date_time_obj)
