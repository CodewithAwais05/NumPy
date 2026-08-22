#   4. Matrix Operations: Multiply two matrices, find inverse, calculate determinant

import numpy as np

matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
matrix2 = np.array([
    [9, 8, 7],
    [6, 52, 4],
    [3, 2, 1]
])

# Matrix Multiplication
print("Multiplication:")
print(matrix1 * matrix2)

# Iverse of a Matrix
print("Inverse of Matrix1:")
print(np.invert(matrix1))

# Determinant of Matrix
print("Determinant:")
print(np.linalg.det(matrix2))