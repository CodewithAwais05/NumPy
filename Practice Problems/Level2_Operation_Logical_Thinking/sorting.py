import numpy as np

arr = np.array([[1, 2, 3], [4, 2, 6]])
print("Original array:\n", arr)

ascending_order = np.sort(arr, axis=None)
print("Array sorted in ascending order:\n", ascending_order)

descending_order = np.sort(arr, axis=None)[::-1]
print("Array sorted in descending order:\n", descending_order)