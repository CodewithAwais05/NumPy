import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Original Array:\n", arr)

second_row = arr[1, :]
print("Second Row:\n", second_row)  # Output: [4 5 6]