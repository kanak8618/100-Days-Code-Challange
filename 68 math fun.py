# Write a function that stutters a word as if someone is struggling to read it.
import math

def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."
 
    stuttered_word = f"{word[:2]}... {word[:2]}... {word}?"
    return stuttered_word

print(stutter("incredible"))

# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)


print(radians_to_degrees(1))

# In this challenge, establish if a given integer num is a Curzon number 2 ** 5 + 1 = 33   2 * 5 + 1 = 11   33 is a multiple of 11

def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

print(is_curzon(5)) 

# Given the side length x find the area of a hexagon. 

def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return round(area, 1)

print(area_of_hexagon(1))

