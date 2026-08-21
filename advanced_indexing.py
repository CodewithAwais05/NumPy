import numpy as np

arr = np.arange(15).reshape(3, 5)

# Boolean indexing with conditions
print(arr[arr > 10])        # [11 12 13 14]
print(arr[(arr > 5) & (arr < 10)])  # [6 7 8 9]

# Where function  (If the element is greater than 7, keep it; otherwise replace it with 0.)
print(np.where(arr > 7, arr, 0))  # Replace <=7 with 0

# Take function  (Take the elements at indices)
indices = [0, 2, 4]
print(np.take(arr[0], indices))  # [0 2 4]

# Choose
choices = [arr, arr*2, arr*3]
print(np.choose(np.array([0,1,2])[:,None], choices))