def multiply_matrix(matrix1, matrix2, result, row, col):
    for i in range(len(matrix1[0])):
        result[row][col] += matrix1[row][i] * matrix2[i][col]

def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for row in range(len(matrix1)):
        for col in range(len(matrix2[0])):
            multiply_matrix(matrix1, matrix2, result, row, col)

    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result = multiply_matrices(matrix1, matrix2)
print(result)  # [[58, 64], [139, 154]]