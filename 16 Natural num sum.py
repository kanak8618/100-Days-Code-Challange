# Write a Python Program to Find the Sum of Natural Numbers.

num = int(input('Enter number :- '))
sum = 0
for i in range(1, num+1):
    sum += i
print(f'Sum of Naturals number is = {sum}')