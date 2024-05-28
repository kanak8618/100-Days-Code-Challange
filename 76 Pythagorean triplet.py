# Create a function that validates whether three given integers form a Pythagorean triplet.

def is_triplet(a, b, c):
 sorted_numbers = sorted([a, b, c])
 return sorted_numbers[0] ** 2 + sorted_numbers[1] ** 2 == sorted_numbers[2] ** 2
 
print(is_triplet(3, 4, 5))

# Create a function that takes a list of strings and return a list, sorted from shortest to longest.

def sort_by_length(lst):
    return sorted(lst, key=len) 
sort_by_length(["Google", "Apple", "Microsoft"])