import numpy as np

#  1. Create a 4x4 array filled with random integers between 1 and 100
random_int = np.random.randint(1, 100, (4,4))
print(random_int)

#  2. Create a 1D array with numbers from 5 to 50 with step 5
numbers = np.arange(5, 51, 5)
print(numbers)

#  3. Create a 3x3 identity matrix
identity = np.eye(3)
print(identity)