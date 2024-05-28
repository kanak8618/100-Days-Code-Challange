# Create a function that takes a list of numbers and return the number that's unique.

def unique(numbers):
    count_dict = {}
 
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    for num, count in count_dict.items():
        if count == 1:
            return num
unique([3, 3, 3, 7, 3, 3])

# Your task is to create a Circle constructor that creates a circle with a radius provided by an argument.

import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def getArea(self):
        return round(math.pi * self.radius**2)
    def getPerimeter(self):
        return round(2 * math.pi * self.radius)

circy = Circle(11)
print(circy.getArea()) 
print(circy.getPerimeter())

"""Create a function that takes an integer and returns a list from 1 to the given number, where:
1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
2. If the number cannot be divided evenly by 4, simply return the number."""

def amplify(num):
    return [n * 10 if n % 4 == 0 else n for n in range(1, num + 1)]
amplify(4)
