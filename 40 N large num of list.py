# Write a Python program to find N largest elements from a list.

def find_n_largest_elements(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    largest_elements = sorted_lst[:n]
    return largest_elements

numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34] 
N = int(input("N = " ))
result = find_n_largest_elements(numbers, N)
print(f"The {N} largest elements in the list are:", result)


# Write a Python program to find smallest number in a list

number = [10,20,30,5,80]
min_number = number[0]
for i in number:
    if i < min_number:
        min_number = i
print("Smallest number of list : " ,min_number)

# Write a Python program to find second largest number in a list.

number = [20,80,60,10,5]
number.sort(reverse=True)
if len(number) >= 2:
    second_largest = number[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number")