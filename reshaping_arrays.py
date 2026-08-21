import numpy as np

arr = np.arange(12)  # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Reshape to 2D arrays

reshape_2D = arr.reshape(4, 3)
print(reshape_2D)


# Reshape to 3D arrays

reshape_3D = arr.reshape(2, 3, 2)
print(reshape_3D)
# print(reshape_3D.ndim)  #  3


# Flatten (Reshape to 1D)

flat = reshape_3D.flatten()  # [0 1 2 3 4 5 6 7 8 9 10 11]
flat_order = reshape_3D.ravel()  # Similar but returns view
print(flat)
print(flat_order)


# Transpose of a matrix (Converting rows into columns and columns into rows)

arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr1)
print(arr1.T)