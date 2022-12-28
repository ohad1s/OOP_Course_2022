import concurrent
from concurrent.futures import ThreadPoolExecutor

def multiply_matrix(matrix1, matrix2, row, col):
    result = 0
    for i in range(len(matrix1[0])):
        result += matrix1[row][i] * matrix2[i][col]
    return (row, col, result)

def multiply_matrices(matrix1, matrix2, num_threads):
    # Create a matrix to store the result
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Create a thread pool with the specified number of threads
    executor= ThreadPoolExecutor(max_workers=num_threads)
    # Create a list of futures to store the results
    futures = []

    # Submit the tasks to the thread pool
    for row in range(len(matrix1)):
        for col in range(len(matrix2[0])):
            futures.append(executor.submit(multiply_matrix, matrix1, matrix2, row, col))

    # Wait for all tasks to complete and retrieve the results
    for future in concurrent.futures.as_completed(futures):
        result[future.result()[0]][future.result()[1]] = future.result()[2]

    return result

# Example usage
matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8], [9, 10], [11, 12]]
result = multiply_matrices(matrix1, matrix2, num_threads=2)
print(result)  # [[58, 64], [139, 154]]
