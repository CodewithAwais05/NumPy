import numpy as np

# Save/Load arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])

# To .npy file
np.save('my_array.npy', arr)
loaded = np.load('my_array.npy')

# To .npz (multiple arrays)
np.savez('multiple.npz', arr1=arr, arr2=arr*2)
data = np.load('multiple.npz')
print(data['arr1'])

# Text files
np.savetxt('array.txt', arr, delimiter=',')
loaded_txt = np.loadtxt('array.txt', delimiter=',')

# CSV
np.savetxt('data.csv', arr, delimiter=',', header='col1,col2,col3')
csv_data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)