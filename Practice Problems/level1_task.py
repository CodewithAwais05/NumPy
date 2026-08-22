#  1. Array Creation: Create a 5x5 matrix with numbers 1-25, then extract the diagonal

import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print("Main Array:")
print(arr)
diagonal = np.diag(arr)
print("Diagonal Elements:")
print(diagonal)