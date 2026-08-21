import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6])
print(arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

# Special arrays

zeros = np.zeros(5)
print(zeros)

ones = np.ones((3, 4))
print(ones)

numbers = np.arange(5, 51, 5)  # np.arange(start, stop, step)
print(numbers)

empty = np.empty((3, 2))
print(empty)

identity = np.eye(4)
print(identity)

full = np.full((2, 3), 4)
print(full)

# Random arrays

random_arr = np.random.random(5)  # Give me 5 random floating-point numbers from [0, 1)
print(random_arr)

random_int = np.random.randint(1, 10, 6) # np.random.randint(start, stop, size)
print(random_int)

normal_dist = np.random.normal(0, 1, 5) # np.random.normal(mean, standard_deviation, size)
print(normal_dist)