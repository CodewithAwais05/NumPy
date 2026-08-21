import numpy as np

arr = np.array([[1, 2, 4], [1, 6, 3]])

print(arr.shape)  # (2, 3) means the array has 2 rows and 3 columns.
print(arr.size)  # 6 means the array contains 6 total elements.
print(arr.ndim)  # 2 means the array has 2 dimensions (rows and columns).
print(arr.dtype)  # int64 means each element is stored as a 64-bit integer.
print(arr.itemsize)  # 8 bytes means each element occupies 8 bytes of memory.
print(arr.nbytes)  # 48 bytes means the entire array uses 48 bytes of memory (6 × 8).


# Different data-types

arr_int = np.array([1, 2, 3], dtype=np.int32)  # Creates an array of 32-bit integers (int32).
print(arr_int)
arr_float = np.array([1, 2, 3], dtype=np.float64)  # Creates an array of 64-bit floating-point numbers (float64).
print(arr_float)
arr_bool = np.array([True, False, True])  # Creates an array containing Boolean values (True/False).
print(arr_bool)
arr_complex = np.array([1+2j, 3+4j])  # Creates an array of complex numbers (a + bj).
print(arr_complex)