# Generate a random date between given start and end dates

import random
from datetime import date, timedelta

def get_random_date(start_date, end_date):
    delta = end_date - start_date
    random_date = start_date + timedelta(days=random.randint(0, delta.days))
    return random_date.strftime('%m/%d/%Y')

d1 = date(int(input('Start year: ')), int(input('Start month: ')), int(input('Start day: ')))
d2 = date(int(input('End year: ')), int(input('End month: ')), int(input('End day: ')))

print("Random Date =", get_random_date(d1, d2))
