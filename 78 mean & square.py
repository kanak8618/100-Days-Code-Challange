# Create a function that returns the mean of all digits

def mean(n):
    n_str = str(n)
    digit_sum = sum(int(digit) for digit in n_str)
    digit_count = len(n_str)
    digit_mean = digit_sum / digit_count
    return int(digit_mean) 
mean(42) 

# Create a function that squares every digit of a number.

def square_digits(n):
    num_str = str(n)
    result_str = ""
    for digit in num_str:
        squared_digit = int(digit) ** 2
    result_str += str(squared_digit)
    return int(result_str)
square_digits(9119) 

# Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not

def is_symmetrical(num):
    num_str = str(num)
    return num_str == num_str[::-1]
is_symmetrical(7227)
