#  capitalizes a letter if its ASCII code is even 

def ascii_capitalize(input_str):
    result = "" 
    for char in input_str:
        if ord(char) % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    return result
    
ascii_capitalize("to be or not to be!")

# Write a function, that replaces all vowels in a string with a specified vowel.

def vow_replace(string, vowel):
    vowels = "aeiou"
    result = ""
    for char in string:
        if char in vowels:
            result += vowel
        else:
            result += char
    return result

vow_replace("apples and bananas", "u")
