# Training instance --> rows
# Features          --> columns

import numpy as np

print("--- Sum by rows and by columns ---")
x = np.array([[1, 2], [3, 4]])

print("x =\n", x)

print("x.sum() = ", x.sum())  # 10

print("x.sum(axis=0) column wise sum = ", x.sum(axis=0))  # [4, 6]

print(x[:, 0].sum(), x[:, 1].sum())  # 4, 6
