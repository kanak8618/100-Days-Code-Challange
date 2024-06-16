# Generate random String of length 5
import random
import string
def randomstring(stringLength):
    """gernerate random string of five characters"""
    letters=string.ascii_letters
    return "".join(random.choice(letters) for i in range(stringLength))
print("random string is ",randomstring(5))

#  Pick a random character from a given String
name="Milind Mali"
char=random.choice(name)
print(char)

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

import random
lottery_tickets_list = []
print("creating 100 random lottery tickets")
for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))

winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)

# Generate 3 random integers between 100 and 999 which is divisible by 5
import random
print("generating three digit number from 100 to 999 which id divisible by 5")
for i in range(3):
    print(random.randrange(100,999,5))