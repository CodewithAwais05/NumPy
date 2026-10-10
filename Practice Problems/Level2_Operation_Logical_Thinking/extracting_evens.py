import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)

even_elements = arr[arr % 2 == 0]
print("Even elements in the array:", even_elements)