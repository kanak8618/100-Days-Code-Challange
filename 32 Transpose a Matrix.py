# Write a Python Program to Transpose a Matrix.

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
 
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

matrix = [
 [1, 2, 3],
 [4, 5, 6]
]

transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print(row)
