import numpy as np

# Creating a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# Reshaping the array into a 2D array
# '-1' allows to calculate the number of rows based on the total number of elements
reshaped_arr = np.reshape(arr, (-1,3,4))

print(reshaped_arr)
