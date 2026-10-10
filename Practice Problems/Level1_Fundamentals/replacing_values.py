import numpy as np

arr = np.arange(1, 11, 1)
print("Original Array:\n", arr)

arr[arr > 5] = 0
print("Modified Array:\n", arr)  # Output: [1 2 3 4 5 0 0 0 0 0]