import numpy as np

arr = np.array([[1, -3, 3], [4, 5, -4]])
print("Original array:\n", arr)

arr[arr < 0] = 0
print("Array after replacing negative values with zero:\n", arr)