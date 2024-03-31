# Write a Python program to Random Password Generator.

import random
import string

print(f"Rendom Number :- {random.randint(1, 100)}")

a = int(input('How Many Pass You want ? : '))
long = int(input('How Much Long pass you want ? : '))


def pass_gen(length):
    select = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits
    password = ''.join(random.choice(select) for _ in range(length)) 
    return password

for i in range(1, a+1):
    generated = pass_gen(long)
    print(f'Password {i} : {generated}')