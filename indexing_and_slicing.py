import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Basic Indexing

print(arr[1, 2])  # 6
print(arr[0, 1])  # 2
print(arr[2, 0])  # 7

# Slicing
#  for 2D (arr[row_start:row_end, column_start:column_end]) # Start is included, End is excluded.

print(arr[0:2, 1:3])  # [[2 3] [5 6]]
print(arr[:, 1])      # [2 5 8] (all rows, column 1)
print(arr[1:, :])     # [[4 5 6] [7 8 9]]


# Boolean indexing
# arr[condition]

condition = arr > 5
print(arr[condition])


# Fancing indexing

index = [0, 2]
print(arr[index])
print(arr[:, 0:2])