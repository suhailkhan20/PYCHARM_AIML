import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 45, endpoint=True)
print("x = ",x)

S = np.sin(x)
C = np.cos(x)

plt.plot(x,S, label='sin curve')
plt.plot(x,C, label='cos curve')
plt.grid(True)
plt.legend(loc='upper left')
plt.show()
