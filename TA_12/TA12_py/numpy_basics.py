import numpy as np


def printSpace():
    print('\n###################################################################################################\n')


printSpace()
# ######################################################################################################################
# Numpy basics usage


# 1. Creating Arrays

# Create a 1D array
b = np.array([1, 2, 3, 4, 5])
print(b)
print(f'type: {type(b)}')
print(f'shape: {b.shape}')
printSpace()


# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(f'type: {type(b)}')
print(f'shape: {b.shape}')
print(f'dimension: {b.ndim}')
print(f'data type: {b.dtype}')
print(f'size: {b.size}')
print(f'item size: {b.itemsize}')
print(f'data: {b.data}')
printSpace()


# Create a 3D array, with type of float 64
b = np.array([[[1, 1], [2, 2],  [3, 3]], [[4, 4], [5, 5], [6, 6]]], dtype=np.float64)
print(b)
print(f'type: {type(b)}')
print(f'shape: {b.shape}')
printSpace()


# Create a 1D array of numbers from 0 to 9
a = np.arange(10)
print(a)
printSpace()


# Create a 3×3 numpy array of all True’s
b = np.ones((3, 3), dtype=bool)
print(b)
printSpace()


# Create a 3×3 numpy array of all Zero's
b = np.zeros((3, 3), dtype=np.float32)
print(b)
printSpace()


# Create an array of evenly spaced values (step value)
b = np.arange(10, 100, 5)
print(b)
printSpace()


# Create an array of evenly spaced values (number of samples)
b = np.linspace(10, 100, 5)
print(b)
printSpace()


# Create a 3x3 identity matrix
b = np.eye(3)
print(b)
printSpace()


# Create an array with random values
b = np.random.random((3, 3))
print(b)
printSpace()

# Extract all odd numbers from array a
c = a[a % 2 == 1]
print(c)
printSpace()


# Replace all odd numbers in array a with -1
a[a % 2 == 1] = -1
print(a)
printSpace()


"""
Data types:
np.int64
np.float32
np.complex
np.bool
np.object
np.string_
"""



# Array Mathematics:
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
c = a + b
print(c)
c = np.add(a, b)
print(c)
printSpace()


# Subtract
c = b - a
print(c)
c = np.subtract(b, a)
print(c)
printSpace()


# Multiply
c = a * b
print(c)
c = np.multiply(a, b)
print(c)
printSpace()


# Divide
c = b / a
print(c)
c = np.divide(b, a)
print(c)
printSpace()


# exponentiation
c = np.exp(a)  # e^a
print(c)
printSpace()


# logarithm
c = np.log(a)  # log_e a
print(c)
printSpace()

# dot product
c = np.dot(a, b)    # a[0]*b[0] + a[1]*b[1] + a[2]*b[2] + a[3]*b[3]
print(c)
printSpace()




# Aggregate Functions:
"""
np.min() - Minimum. The minimum value along a given axis.
np.max() - Maximum. The maximum value along a given axis.
np.argmin() - Index of the minimum. The index of the minimum value along a given axis.
np.argmax() - Index of the maximum. The index of the maximum value along a given axis.
np.median() - Median. The median along a given axis.
np.mean() - Arithmetic mean. Zero-length arrays have NaN mean.
np.sum() - Sum of all the elements in the array or along an axis. Zero-length arrays have sum 0.
np.prod() - Product of all the elements in the array or along an axis. One-length arrays have product 1.
np.std() - Standard deviation. Zero-length arrays have NaN standard deviation.
np.var() - Variance. Zero-length arrays have NaN variance.
np.percentile() - Percentile. The q-th percentile of the data along a given axis.
np.any() - Logical OR. Evaluates whether any elements are true.
np.all() - Logical AND. Evaluates whether all elements are true.
np.corrcoef() - Correlation coefficient.
np.cov() - Covariance.
np.cumsum() - Cumulative sum. Returns the cumulative sum of the elements along a given axis.
"""



a = np.arange(10)
print(a)
print(f'cumulative sum: \n{np.cumsum(a)}')
printSpace()


print(f'mean: {np.mean(a)}')
print(f'median: {np.median(a)}')
print(f'sum: {np.sum(a)}')
print(f'product: {np.prod(a)}')
print(f'standard deviation: {np.std(a)}')
print(f'variance: {np.var(a)}')
print(f'percentile: {np.percentile(a, 50)}')
print(f'any: {np.any(a)}')
print(f'all: {np.all(a)}')
printSpace()



"""
np.linalg

np.linalg.matrix_rank() - Compute the rank of a matrix.
np.linalg.solve() - Solve the linear system Ax = b for x, where A is a square matrix.
np.linalg.matrix_power() - Raise a square matrix to the (integer) power n.
np.linalg.orth() - Return a (modified) Gram-Schmidt orthonormal basis for the vectors in a.
np.linalg.det() - Compute the determinant of an array.
np.linalg.eig() - Compute the eigenvalues and right eigenvectors of a square array.
np.linalg.inv() - Compute the (multiplicative) inverse of a matrix.
np.linalg.pinv() - Compute the Moore-Penrose pseudo-inverse inverse of a matrix.
np.linalg.qr() - Compute the QR decomposition of a matrix.
np.linalg.svd() - Compute the singular value decomposition (SVD) of a matrix.
np.linalg.lstsq() - Compute the least-squares solution to y = Xb.
np.linalg.eigvals() - Compute the eigenvalues of a general matrix.
np.linalg.eigh() - Compute the eigenvalues and eigenvectors of a Hermitian or symmetric matrix.
np.linalg.eigvalsh() - Compute the eigenvalues of a Hermitian or symmetric matrix.
np.linalg.norm() - Matrix or vector norm.
np.linalg.cond() - Compute the condition number of a matrix.
np.linalg.slogdet() - Compute the sign and (natural) logarithm of the determinant of an array.
np.linalg.tensorsolve() - Solve the tensor equation a x = b for x.
np.linalg.tensorinv() - Compute the 'inverse' of an N-dimensional array.
np.linalg.cholesky() - Compute the Cholesky decomposition of a matrix.
np.linalg.cho_factor() - Cholesky factorization of a matrix.
np.linalg.cho_solve() - Solve the linear system a x = b given the Cholesky factorization a = cho_factor(a).
np.linalg.lu() - Compute the LU decomposition of a matrix.
np.linalg.lu_factor() - LU decomposition of a matrix.
np.linalg.lu_solve() - Solve the linear system a x = b given the LU factorization a = lu_factor(a).
np.linalg.svdvals() - Compute the singular values of a matrix.
np.linalg.multi_dot() - Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order.
np.linalg.matrix_balance() - Compute a similarity transformation to improve the conditioning of a matrix.
np.linalg.matrix_fraction() - Compute the matrix fraction, a/b, where a and b are square matrices.
np.linalg.matrix_power() - Raise a square matrix to the (integer) power n.
np.linalg.fractional_matrix_power() - Raise a square matrix to the (real) power n.
np.linalg.solve_banded() - Solve a linear matrix equation, or system of linear scalar equations for x, given a banded matrix A and a right-hand side.
np.linalg.solveh_banded() - Solve a linear matrix equation, or system of linear scalar equations for x, given a banded Hermitian or symmetric matrix A and a right-hand side.
"""


a = np.arange(12)
print(a)
a = a.reshape((4, 3))
print(a)
