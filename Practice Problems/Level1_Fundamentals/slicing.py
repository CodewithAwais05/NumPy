import numpy as np

arr = np.arange(1, 21, 1)
print("Original Array:\n", arr)

first_five = arr[:5]
print("First Five Elements:\n", first_five)  # Output: [1 2 3 4 5]

last_five = arr[-5:]
print("Last Five Elements:\n", last_five)  # Output: [16 17 18 19 20]

every_second = arr[::2]
print("Every Second Element:\n", every_second)  # Output: [1 3 5 7 9 11 13 15 17 19]