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

#Generate a random Password which meets the following conditions
import random
import string
def randomPassword():
    password=random.sample(randomSource,6)
    randomSource=string.ascii_letters+string.digits+string.punctuation
    password+=random.sample(string.ascii_uppercase,2)
    password+=random.choice(string.digits)
    password+=random.choice(string.punctuation)
    passwordList=list(password)
    random.SystemRandom().shuffle(passwordList)
    password="".join(passwordList)
    return password
print("password is: ",randomPassword())

