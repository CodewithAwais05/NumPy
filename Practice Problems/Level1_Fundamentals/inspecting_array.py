import numpy as np

arr = np.arange(1, 13, 1).reshape(3, 4)
print(arr)

print("Dimensions:", arr.ndim)  # Output: 2
print("Shape:", arr.shape)  # Output: (3, 4)
print("Size:", arr.size)  # Output: 12
print("Data Type:", arr.dtype)  # Output: int64 (or int32 depending on the system)