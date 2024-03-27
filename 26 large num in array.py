# Write a Python Program to find largest element in an array.

def find_largest_element(arr):
    if not arr:
        return "Array is empty"
    largest_element = arr[0]
    for element in arr:
        if element > largest_element:
            largest_element = element
            return largest_element

my_array = [10, 20, 30, 99]
result = find_largest_element(my_array)
print(f"The largest element in the array is: {result}")
