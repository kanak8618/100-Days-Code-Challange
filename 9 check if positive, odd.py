# Write a Python Program to Check if a Number is Positive, Negative or Zero.

num1 = int(input('Enter Number :- '))

if num1 > 0:
    print(f'{num1} number is Positive')
elif num1 == 0:
    print(f'{num1} is Zero')
else:
    print(f'{num1} number is Negative')

# Write a Python Program to Check if a Number is Odd or Even.

num1 = int(input('Enter Number :- '))

if num1%2 == 0:
    print(f'{num1} is Even Number')
else:
    print(f'{num1} is Odd Number')