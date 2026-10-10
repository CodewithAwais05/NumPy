import numpy as np

arr = np.array([[1, 2, 0], [4, 5, -4]])
print("Original array:\n", arr)

positive_count = np.sum(arr > 0)
negative_count = np.sum(arr < 0)
zero_count = np.sum(arr == 0)

print("Count of positive numbers in the array:", positive_count)
print("Count of negative numbers in the array:", negative_count)
print("Count of zeros in the array:", zero_count)
