"""ssignment Taks: Image Pixel Analysis

Description:
Simulate a grayscale image as a 8x8 array with pixel values (0-255)"""

import numpy as np

# a) Task: Generate random pixel values in an 8x8 grayscale image
np.random.seed(42)  # For reproducibility
image = np.random.randint(0, 256, size=(8, 8))
print("Original Image (Pixel Values 0–255):\n", image)

# b) Task: Normalize pixels to range 0.0–1.0
normalized_image = image / 255.0
print("\nNormalized Image (0.0–1.0):\n", normalized_image)

# c) Task: Detect bright pixels (value > 200)
bright_pixels_mask = image > 200
print("\nBright Pixels (value > 200):\n", bright_pixels_mask)

# d) Task: Apply filter – set pixels < 50 to 0
filtered_image = np.copy(image)
filtered_image[filtered_image < 50] = 0
print("\nFiltered Image (pixels < 50 set to 0):\n", filtered_image)

# e) Task: Calculate histogram with bins: 0, 50, 100, 150, 200, 255
hist, bin_edges = np.histogram(image, bins=[0, 50, 100, 150, 200, 255])
print("\nHistogram (Bins = [0, 50, 100, 150, 200, 255]):")
print("Counts:", hist)
print("Bin Edges:", bin_edges)