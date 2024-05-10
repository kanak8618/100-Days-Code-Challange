# Write a program that calculates and prints the value according to the given formula:
# 𝑄 = Square root of 2𝐶𝐷/𝐻    C is 50. H is 30

import math
C = 50
H = 30
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))
input_sequence = input("Enter comma-separated values of D: ")
D_values = input_sequence.split(',')
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))

# Write a program which takes 2 digits, X,Y as input and generates a 2D array

X, Y = map(int, input("Enter two digits (X, Y): ").split(','))
array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
for row in array:
    print(row)
