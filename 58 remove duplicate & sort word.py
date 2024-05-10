# Remove duplicate and sorting words

input_sequence = input("Enter a sequence of whitespace-separated words: " )
words = set(input_sequence.split())
sorted_words = sorted(words)
result = ' '.join(sorted_words)
print("Result:", result)

# Write a program count letters and numbers in string

sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print("LETTERS", letter_count)
print("DIGITS", digit_count)
