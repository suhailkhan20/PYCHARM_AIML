import numpy as np
import matplotlib.pyplot as plt

# Create a figure of size 6x4 inches, 80 dots per inch
# Note: One of the provided images shows figsize=(8, 6)
plt.figure(figsize=(6, 4))

# Create arrays for the x-axis, sine, and cosine values
X = np.linspace(-np.pi, np.pi, num=255, endpoint=True)
S = np.sin(X)
C = np.cos(X)

# Plot sine with a red continuous line of width 5.0
# Note: The comment in the image says "green continuous line"
plt.plot(X, S, color="red", linewidth=5.0, linestyle="-", label="sine curve")

# Plot cosine with a blue dashed line of width 7.0
# Note: The comment in the image says "blue continuous line"
plt.plot(X, C, color="blue", linewidth=7.0, linestyle="--", label="cosine curve")

# Add a legend to the upper left corner
plt.legend(loc='upper left')

# Set the limits for the x-axis
plt.xlim(-4.0, 4.0)

# Set the tick marks for the x-axis
plt.xticks(np.linspace(-4, 4, num=9, endpoint=True))

# Display the plot
plt.show()