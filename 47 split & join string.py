# Write a Python program to split and join a string.

input_str = str(input("Enter String :- "))

word_list = input_str.split() 
separator = " "
output_str = separator.join(word_list)

print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)
