# Write a Python program to Count occurrences of an element in a list.

def count_occurrences(l, element):
    count = l.count(element)
    return count
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurrences} times in the list")
