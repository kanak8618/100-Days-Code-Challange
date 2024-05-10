# Write a Python program to Merging two Dictionaries. 

# 1. Using the update() method:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print("Merged Dictionary (using update()):", dict1)

# 2. Using dictionary unpacking
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary (using dictionary unpacking):", merged_dict)
