# Random concept

import numpy as np
res1 = np.random.rand(4)
print("res1:",res1)

np.random.seed(1)
res2 = np.random.rand(8)
print("res2:",res2)

np.random.seed(2)
res3 = np.random.rand(2)
print("res3:",res3)

np.random.seed(1)
res5 = np.random.rand(2,4)
print('res5:',res5)

np.random.seed(3)
res3 = np.random.rand(4)
print('res3:',res3)

