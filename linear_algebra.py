import numpy as np

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Dot product
print(np.dot(A, B))  # or A @ B
# [[19 22]
#  [43 50]]

# Matrix inverse
print(np.linalg.inv(A))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

# Determinant
print(np.linalg.det(A))  # -2.0

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Solve linear equations
# 3x + 2y = 8``
# x + 4y = 11
coeff = np.array([[3, 2], [1, 4]])
const = np.array([8, 11])
solution = np.linalg.solve(coeff, const)
print(solution)  # [1. 2.5]

# Matrix decomposition
U, S, V = np.linalg.svd(A)  # Singular Value Decomposition