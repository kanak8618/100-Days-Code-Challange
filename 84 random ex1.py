#  Roll dice in such a way that every time you get the same number

import random
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))

#Generate random secure token of 64 bytes and random URL
import secrets
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

#  Calculate multiplication of two random float numbers
num1=random.random()
num2=random.uniform(9.5,99.5)
num3=num1+num2
print(num3)


