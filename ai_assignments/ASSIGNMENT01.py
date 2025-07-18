# Create a 1D Array
#Task: Create a 1D array containing the numbers [10, 20, 30, 40, 50].
import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
print("arr1 =" ,arr1)

#Assignment 2: Generate a Sequence
#Task: Generate an array of 15 evenly spaced numbers from 0 to 5 (inclusive).
arr2 = np.linspace(0, 5, 15)
print("arr2 =",arr2)

#Assignment 3: Matrix of Zeros
#Task: Create a 4x3 matrix (4 rows, 3 columns) filled with zeros.
arr3 = np.zeros((4, 3))
print("arr3 =",arr3)

#Assignment 4: Element-wise Operations
#Task: Given arr = np.array([2, 4, 6, 8]), compute a new array where each element is squared.
arr4 = np.array([2, 4, 6, 8])
squared_arr = arr4 ** 2
print("sqr arr4 =",squared_arr)

#Assignment 5: Boolean Filtering
#Task: From arr = np.array([3, 11, 7, 9, 15]), extract all values greater than 7.
arr5 = np.array([3, 11, 7, 9, 15])
filtered_arr = arr5[arr5 > 7]
print("filtered arr=",filtered_arr)
