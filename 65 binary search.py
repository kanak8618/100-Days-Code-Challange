# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1 # Target is in the right half
        else:
            right = mid - 1 # Target is in the left half
    return -1 # Element not found in the list

sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 4
result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")