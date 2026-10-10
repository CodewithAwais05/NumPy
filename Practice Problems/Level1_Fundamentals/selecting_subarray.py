import numpy as np

arr = np.arange(1, 26, 1).reshape(5, 5)
print("Original Array:\n", arr)

subarray = arr[1:4, 1:4]
print("Selected Subarray:\n", subarray)  # Output: [[ 7  8  9]
                                                #   [12 13 14]
                                                #   [17 18 19]]