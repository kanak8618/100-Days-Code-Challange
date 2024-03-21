# Write a Python program to swap two variables.

# Method 1
num1, num2 = int(input('Enter Num1 :- ')), int(input('Enter Num2 :- '))

temp = num1+num2
num1 = temp-num1
num2 = temp-num2

print(f"Swap Value \nnum1 = {num1} \nnum2 = {num2} ")

# Method 2
temp = num1
num1 = num2
num2 = temp

print(f"Swap Value \nnum1 = {num1} \nnum2 = {num2} ")


# Write a Python program to swap two variables without 3rd vaiable

# Method 3
num1 = num1+ num2
num2 = num1-num2
num1 = num1-num2
print(f"Swap Value \nnum1 = {num1} \nnum2 = {num2} ")

# Method 4
num1, num2 = num2, num1
print(f"Swap Value \nnum1 = {num1} \nnum2 = {num2} ")
