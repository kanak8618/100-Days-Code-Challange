# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
 
def filter_list(lst):
    result = []
 
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)
 
    return result
filter_list([1, 2, "a", "b"]) 
