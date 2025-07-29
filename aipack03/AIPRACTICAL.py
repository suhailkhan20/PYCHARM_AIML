import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
x = np.sin(25 * z)
y = np.cos(25 * z)

ax.plot(x, y, z, 'red')
ax.set_title('3D Line Plot')
plt.show()