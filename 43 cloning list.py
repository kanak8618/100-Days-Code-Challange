# Write a Python program to Cloning or Copying a list

original_list = [1,2,3,4,5]

# 1. Using the Slice Operator
copy_list = original_list[:]
print('Cloned List',copy_list)

# 2. Using the list() constructor
copy_list = list(original_list)
print('Cloned List',copy_list)

# 3. Using List Comprehension
copy_list = [item for item in original_list]
print('Cloned List',copy_list)