# Practical-41

import numpy as np

# Creating a 1D NumPy array
arr = np.array([1, 2, 3, 4, 5, 6,7,8,9,10,11,12])

# Reshaping the 1D array into a 2D array with 2 rows and 3 columns
reshaped_arr = np.reshape(arr, (12,1))
print(reshaped_arr)
