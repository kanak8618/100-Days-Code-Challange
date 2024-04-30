# Write a Python program to check if the given number is a Disarium Number

"""A Disarium number is a number that is equal to the sum of its digits each raised to the
power of its respective position. 8¹+9² = 8+81=89"""

def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number

try:
    num = int(input("Enter a number: "))
    if is_disarium(num):
        print(f"{num} is a Disarium number.")
    else:
        print(f"{num} is not a Disarium number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")


# Write a Python program to print all disarium numbers between 1 to 100.

def is_disarium(num):
    num_str = str(num)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return num == digit_sum
disarium_numbers = [num for num in range(1, 101) if is_disarium(num)]
print("Disarium numbers between 1 and 100:")
for num in disarium_numbers:
    print(num, end=" | ")
