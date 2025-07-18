#Assignment 6
# Task: Convert arr = np.arange(12) into a 3x4 matrix.
import numpy as np

arr6 = np.arange(12)
reshaped_arr = arr6.reshape(3, 4)
print("reshaped arr =",reshaped_arr)

#assignment07
# Task: Compute the dot product of a = np.array([1, 2, 3]) and b = np.array([4, 5, 6]).

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
dot_product = np.dot(a, b)  # or use a @ b
print("Dot product of arr =",dot_product)

#assignment08
# Task: From matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# extract the sub-matrix [[2, 3], [5, 6]].

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
sub_matrix = matrix[0:2, 1:3]
print("sub matrix =",sub_matrix)

#assignment09
# Task: For data = [5, 12, 8, 3, 9], compute the mean and maximum value.

data = np.array([5, 12, 8, 3, 9])
mean_val = np.mean(data)
max_val = np.max(data)
print("Mean:", mean_val)
print("Max:", max_val)

#assignment10
# Task: Vertically stack a = [1, 2, 3] and b = [4, 5, 6] into a 2x3 matrix.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked = np.vstack((a, b))
print("stacked =",stacked)
