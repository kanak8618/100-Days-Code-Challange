# Calculate the date 4 months from the current date

from dateutil.relativedelta import relativedelta

given_date = datetime(2020, 2, 25).date()
months_to_add=4
result_date=given_date+relativedelta(months= + months_to_add)
print(result_date)
