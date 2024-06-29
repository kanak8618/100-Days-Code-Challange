# Generate 3 random integers between 100 and 999 which is divisible by 5
import random
print("generating three digit number from 100 to 999 which id divisible by 5")
for i in range(3):
    print(random.randrange(100,999,5))


#Generate a random Password which meets the following conditions
import random
import string
def randomPassword():
    password=random.sample(rs,6)
    rs=string.ascii_letters+string.digits+string.punctuation
    password+=random.sample(string.ascii_uppercase,2)
    password+=random.choice(string.digits)
    password+=random.choice(string.punctuation)
    passwordList=list(password)
    random.SystemRandom().shuffle(passwordList)
    password="".join(passwordList)
    return password
print("password is: ",randomPassword())
