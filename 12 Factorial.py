# Write a Python Program to Find the Factorial of a Number.

num1 = int(input("Enter NUmbr :- "))
fact = 1
if num1 < 0:
    print(f"not posible for {num1} ")
elif num1 == 0:
    print("not possible for 0")
else:
    for i in range(1, num1+1):
        fact = fact * i
    print(f"factorial of {num1} = {fact}")