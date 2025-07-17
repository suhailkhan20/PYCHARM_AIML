# Practical-35

import numpy as np

n4 = np.array([10, -1, 0, 90, 300, 3, -6, 2])
print("Before : n4 =", n4)

# External sorting
n5 = sorted(n4, reverse=True)
print("n5 =", n5)
print("After : n4 =", n4)

# Internal sorting or In-place sorting
n4.sort()
print("After n4.sort() =", n4)
print("After n4.sort() =", list(reversed(n4)))
print("After n4.sort() =", tuple(reversed(n4)))
# print("After n4.sort() =", dict(reversed(n4)))
print("After n4.sort() =", set(reversed(n4)))