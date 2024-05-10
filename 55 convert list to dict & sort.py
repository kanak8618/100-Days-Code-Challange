# Write a Python program to convert key-values list to flat dictionary.

key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {}
for key, value in key_values_list:
    flat_dict[key] = value
print("Flat Dictionary:", flat_dict)

# Write a Python program to sort Python Dictionaries by Key or Value.

# Sort by Keys:
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by keys:")
for key, value in sorted_dict_by_keys.items():
    print(f"{key}: {value}")

# Sort by values
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_values = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")

