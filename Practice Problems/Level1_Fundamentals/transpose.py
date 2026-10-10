import numpy as np

arr = np.arange(1, 13, 1).reshape(3, 4)
print("Original Array:\n", arr)

transposed_arr = arr.T
print("Transposed Array:\n", transposed_arr)  # Output: [[ 1  5  9]
                                                #        [ 2  6 10]
                                                #        [ 3  7 11]
                                                #        [ 4  8 12]]