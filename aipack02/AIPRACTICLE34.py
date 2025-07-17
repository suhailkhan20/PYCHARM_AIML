import numpy as np

n1 = np.array([4, 5, 6])
print("n1 * 2 = ", n1 * 2)

n2 = np.array([1, 2, 3])

print("n1 = ", n1)           # [4, 5, 6]
print("n2 = ", n2)           # [1, 2, 3]
print("n1 + n2 = ", n1 + n2)

n3 = np.array([4, 5, 6])
print(n1 + n3)   # It will produce error due to shape mismatch

print("n1 = ", n1+n2)
print("n2 = ", n1-n2)
