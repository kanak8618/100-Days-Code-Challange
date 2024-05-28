# Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.

def mapping(letters):
    result = {}
    for letter in letters:
        result[letter] = letter.upper()
    return result
mapping(["p", "s"]) 

# Write a function that converts a dictionary into a list of keys-values tuples.

def dict_to_list(input_dict):
    sorted_dict = sorted(input_dict.items())
    result = [(key, value) for key, value in sorted_dict]
    return result

dict_to_list({"D": 1, "B": 2, "C": 3})