# Write a Python Program to Find Factorial of Number Using Recursion.

def recur_facto(n):
    if n == 1:
        return n
    else:
        return n * recur_facto(n-1)

num = int(input('Enter Number : '))

if num < 0:
    print('not available')
elif num == 0:
    print('Factorial of 0 is 1')
else:
    print(f'Factorial of {num} is {recur_facto(num)}')