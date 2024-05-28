# Write a function that moves all elements of one type to the end of the list.

def move_to_end(lst, element):
    count = lst.count(element)
    lst = [x for x in lst if x != element]
    lst.extend([element] * count)
    return lst
move_to_end([1, 3, 2, 4, 4, 1], 1)

# Create a function that takes a string and returns a string in which each character is repeated once.

def double_char(input_str):
    doubled_str = ""
    for char in input_str:
        doubled_str += char * 2
    return doubled_str
double_char("String")

# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

def reverse(value):
    if isinstance(value, bool):
        return not value
    else:
        return "boolean expected"
reverse(True) 

# Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself.

def add_indexes(lst):
    return [i + val for i, val in enumerate(lst)]
add_indexes([0, 0, 0, 0, 0]) 

