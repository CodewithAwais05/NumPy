import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 1], [10, 6, 12]])

difference_elements = np.setdiff1d(arr1, arr2)
print("Elements in arr1 that are not in arr2:", difference_elements)