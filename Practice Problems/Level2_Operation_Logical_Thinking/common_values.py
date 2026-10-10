import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 2], [10, 6, 12]])

common_elements = np.intersect1d(arr1, arr2)
print("Common elements between the two arrays:", common_elements)