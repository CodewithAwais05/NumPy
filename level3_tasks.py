import numpy as np

#  1. Create a 5x5 matrix where all border elements are 1 and inside is 0

matrix = np.zeros((5, 5), dtype=int)

matrix[0, :] = 1    # first row and all columns
matrix[-1, :] = 1   # last row and all columns
matrix[:, 0] = 1    # all rows and first column
matrix[:, -1] = 1   # all rows and last column

print(matrix)


#  2. Normalize a 10x10 random array (subtract mean, divide by std)

array = np.arange(100).reshape(10, 10)
normalized = (array - np.mean(array)) / np.std(array)
print(normalized)

# if mean = 0 and std = 1 then matrix is normalized
print("Mean", np.mean(normalized))
print("STD", np.std(normalized))

