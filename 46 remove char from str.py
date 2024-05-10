# Write a Python program for removing 𝑖 character from a string

def remove_char(input_str, i):
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
    result_str = input_str[:i] + input_str[i + 1:]
    return result_str

input_str = "Hello, wWorld!"
i = int(input("Enter Index NUmber : "))
new_str = remove_char(input_str, i)
print(f"Original String: {input_str}")
print(f"String after removing {i}th character : {new_str}")
