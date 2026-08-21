import numpy as np

#  1. Create a 1D array of 20 elements and reshape it to 4x5

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
reshaped_array = arr.reshape(4, 5)
print(reshaped_array)


#  2. Extract all elements greater than 10 from a 5x5 random array

array = np.array([
    [1, 20, 3, 4, 5],
    [6, 1, 8, 54, 10],
    [11, 12, 543, 14, 15],
    [16, 17, 234, 19, 20],
    [21, 32, 23, 0, 25]
])

condition = array > 10
print(array[condition])


#  3. Replace all even numbers in an array with 0

arrays = np.array([
    [1, 20, 3, 4, 5],
    [6, 1, 8, 54, 10],
    [11, 12, 543, 14, 15],
    [16, 17, 234, 19, 20],
    [21, 32, 23, 0, 25]
])
arrays[arrays % 2 == 0] = 0
print(arrays)