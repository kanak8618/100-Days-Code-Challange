"""Write a program to compute the frequency of the words from the input. The output
should output after sorting the key alphanumerically. Suppose the following input is
supplied to the program: New to Python or choosing between Python 2 and Python 3? Read Python 2 or
Python 3."""

input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
word_freq = {}
for word in words:
    word = word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items())
for word, frequency in sorted_words:
    print(f"{word}:{frequency}")
