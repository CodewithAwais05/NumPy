import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Original Array:\n", arr)

third_column = arr[:, 2]
print("Third Column:\n", third_column)  # Output: [3 6 9 12]