import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)

index_of_max = np.argmax(arr)
print("Index of maximum value in the array:", index_of_max)

index_of_min = np.argmin(arr)
print("Index of minimum value in the array:", index_of_min)