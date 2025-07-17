import numpy as np

x = np.full((5,7),7,dtype=int)

print("x =\n", x)


print("sum of one row: ",x[1, :].sum())
print("sum of one column: ",x[:, 1].sum())