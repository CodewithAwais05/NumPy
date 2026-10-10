import numpy as np

arr = np.arange(1, 25, 1)
print("Original Array:\n", arr)

reshaped_arr = arr.reshape(4, 6)
print("Reshaped Array:\n", reshaped_arr)

reshaped_arr_2 = arr.reshape(3, 8)
print("Another Reshaped Array:\n", reshaped_arr_2)