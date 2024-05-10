# Write a Python Program to check if a string contains any special character.

import re
def check_special_char(in_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'
    if re.search(pattern, in_str):
        return True
    else:
        return False
        
input_string = str(input("Enter a string: "))
contains_special = check_special_char(input_string)
if contains_special:
    print("The string contains special characters.")
else:
    print("The string does not contain special characters.")