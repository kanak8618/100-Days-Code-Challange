# Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".

def is_isogram(word):
    word = word.lower()
    unique_letters = set()
    for letter in word:
        if letter in unique_letters:
            return False
    unique_letters.add(letter)
    return True
is_isogram("Algorism")

# A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

def society_name(names):
    secret_name = ''.join(sorted([name[0] for name in names]))
    return secret_name
society_name(["Adam", "Sarah", "Malcolm"])
