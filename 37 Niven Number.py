#Write a Python program to determine whether the given number is a Harshad Number.

"""A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
   18 is a Harshad number because ,1+8=9, and 18 is divisible by 9"""

def is_harshad_number(num):
    digit_sum = sum(int(i) for i in str(num))
    return num % digit_sum == 0

num = int(input("Enter a number: "))

if is_harshad_number(num):
    print(f"{num} is a Harshad Number.")
else:
    print(f"{num} is not a Harshad Number.")
