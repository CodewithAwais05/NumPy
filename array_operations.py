import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

# Arithmatic Operations

print(arr1 + arr2)   # [ 6  8 10 12]
print(arr1 - arr2)   # [-4 -4 -4 -4]
print(arr1 * arr2)   # [ 5 12 21 32]
print(arr1 / arr2)   # [0.2        0.33333333 0.42857143 0.5       ]
print(arr1 ** 2)     # [ 1  4  9 16]

# Broadcasting

scalar = 3
print(arr1 * scalar)  # [ 3  6  9 12]

# Universal functions

array = np.array([1, 76, 34, 65, 36])
arr = np.array([1, -5, 3, -8, -3, -5])
print(np.sqrt(array))   # [1.         8.71779789 5.83095189 8.06225775 6.        ]
print(np.exp(array))    # [2.71828183e+00 1.01480039e+33 5.83461743e+14 1.69488924e+28 4.31123155e+15]
print(np.abs(arr))      # [1 5 3 8 3 5]
print(np.log(array))    # [0.         4.33073334 3.52636052 4.17438727 3.58351894]
print(np.sin(array))    # [ 0.84147098  0.56610764  0.52908269  0.82682868 -0.99177885]
print(np.cos(array))    # [ 0.54030231  0.82433133 -0.84857027 -0.56245385 -0.12796369]