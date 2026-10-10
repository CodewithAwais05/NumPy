import numpy as np

arr1 = np.arange(1, 21, 1)
arr2 = np.arange(21, 41, 1)
print("Array 1:\n", arr1)
print("Array 2:\n", arr2)

print("Concatenated Array:\n", np.concatenate([arr1, arr2]))  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40]

print("Vertically Stacked Array:\n", np.vstack([arr1, arr2]))  # Output: [[ 1  2  3  4  5  6  7  8  9 10]
                                                #         [21 22 23 24 25 26 27 28
                                                #          29 30 31 32 33 34 35 36 37 38 39 40]]

print("Horizontally Stacked Array:\n", np.hstack([arr1, arr2]))  # Output: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40]