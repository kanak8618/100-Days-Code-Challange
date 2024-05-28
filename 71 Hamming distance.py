# Hamming distance is the number of characters that differ between two strings.

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1 # Increment the counter for differences
    return distance

    
print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))