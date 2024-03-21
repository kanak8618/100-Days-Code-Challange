# Write a Python program to do arithmetical operations +, - , * , / 

#addition
num1 = float(input('Enter Number :- '))
num2 = float(input('Enter Number :- '))
sum = num1 + num2
print(f"{num1} + {num2} = {sum}")

#substraction
num1 = float(input('Enter Number :- '))
num2 = float(input('Enter Number :- '))
sub = num1 - num2
print(f"{num1} - {num2} = {sub}")

#multiplication
num1 = float(input('Enter Number :- '))
num2 = float(input('Enter Number :- '))
mul = num1 * num2
print(f"{num1} * {num2} = {mul}")

#Division
num1 = float(input('Enter Number :- '))
num2 = float(input('Enter Number :- '))
print('not Possible' if num2 == 0 else f"{num1} / {num2} = {num1/num2}")
# print('not Possible') if num2 == 0 else print(f"{num1} / {num2} = {num1/num2}")


#Arithmetic Operation
num1, num2  = float(input('Enter number :- ')), float(input('Enter number :- '))
print('Addition + : \nSubstraction - : \nMultplication * : \nDivision / :')
choice = input('Enter Your Choice :- ')

match choice:
    case '+': print(f"{num1} + {num2} = {num1 + num2}")
    case '-': print(f"{num1} - {num2} = {num1 - num2}")
    case '*': print(f"{num1} * {num2} = {num1 * num2}")
    case '/' if num2 > 0: print(f"{num1} / {num2} = {num1 / num2}")
    case _: print('!!! invalid choice !!!')