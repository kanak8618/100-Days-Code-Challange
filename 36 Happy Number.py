# Write a Python program to check if the given number is Happy Number

"""A happy number is a number that eventually reaches 1 when replaced by the sum of the square of each digit. 
Numbers that loop endlessly in this process are not happy numbers"""

def is_happy_number(num):
    def get_next(n):
        next_num = 0
        while n > 0:
            n, digit = divmod(n, 10)
            next_num += digit ** 2
        return next_num
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = get_next(num)
    return num == 1

try:
    num = int(input("Enter a number: "))
    if is_happy_number(num):
        print(f"{num} is a Happy Number.")
    else:
        print(f"{num} is not a Happy Number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
