import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr1 = np.array([[1, 2], [3, 4], [5, 6]])
print(np.mean(arr1))

print(np.sum(arr))          # 45
print(np.mean(arr))         # 5.0
print(np.median(arr))       # 5.0
print(np.std(arr))          # 2.581...
print(np.var(arr))          # 6.666...
print(np.min(arr))          # 1
print(np.max(arr))          # 9
print(np.argmin(arr))       # 0 (index of min)
print(np.argmax(arr))       # 8 (index of max)

# Axis-specific operations
print(np.sum(arr, axis=0))  # [12 15 18] (column sums)
print(np.sum(arr, axis=1))  # [6 15 24] (row sums)
print(np.mean(arr, axis=0)) # [4. 5. 6.]