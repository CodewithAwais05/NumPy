# -----------------------------------------------------------------
# Broadcasting allows operations on arrays of different shapes.
# -----------------------------------------------------------------

import numpy as np

# 1D + scalar
arr = np.array([1, 2, 3])
print(arr + 5)  # [6 7 8]

# 2D + 1D
matrix = np.array([[1, 2, 3], [4, 5, 6]])
vector = np.array([10, 20, 30])
print(matrix + vector)

# Broadcasting rules
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[10], [20]])
print(a * b)