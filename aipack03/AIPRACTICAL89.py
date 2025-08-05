
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = [1,2,3,4,5,6,7,8,9,10]
y1 = np.random.randint(low=0, high=10, size=10)
z1 = np.random.randint(low=0, high=10, size=10)

x2 = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
y2 = np.random.randint(low=-10, high=0, size=10)
z2 = np.random.randint(low=0, high=10, size=10)

ax.scatter(x1, y1, z1, c='b', marker='o', label='star')
ax.scatter(x2, y2, z2, c='r', marker='o', label='real')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.title("3D Scatter Plot Example")
plt.legend()
plt.show()
