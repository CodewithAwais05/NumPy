import numpy as np

# Concatenation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.vstack((a, b))  # Vertical stack (It puts b below a.)(vstack = vertical = rows increase)
print(result) 
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

result = np.hstack((a, b))  # Horizontal stack (b is placed beside a.)(hstack = horizontal = columns increase)
print(result)  
# [[1 2 5 6]
#  [3 4 7 8]]

# Splitting 
arr = np.arange(12).reshape(3, 4)
print(np.split(arr, 3))  # Split this array into 3 equal parts.

# Adding/removing dimensions
arr = np.array([1, 2, 3])
print(arr[np.newaxis, :])  # [[1 2 3]] (add row dimension)
print(arr[:, np.newaxis])  # [[1] [2] [3]] (add column dimension)

# Squeeze (remove singleton dimensions) (np.squeeze() removes dimensions whose size is exactly 1.)
arr = np.array([[[1, 2, 3]]])  # Shape (1, 1, 3)
print(np.squeeze(arr))  # [1 2 3] (shape 3)