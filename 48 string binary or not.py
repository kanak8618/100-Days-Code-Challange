# Write a Python program to check if a given string is binary string or not.

def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False 
    return True 

input_str = input("Enter String :-")
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
