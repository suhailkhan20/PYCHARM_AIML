"""Assignment Task: Student Grade Statistics

Description:
Process grades of 10 students across 4 subjects (Math, Science, English, History).
Create a 10x4 array with random scores (0-100). """

import numpy as np

# Task: Create a 5x7 NumPy array with random temperatures between 10°C and 35°C
# (5 cities × 7 days)
np.random.seed(0)  # For reproducibility
temps = np.random.randint(10, 36, size=(5, 7))
print("Temperature Data (°C):\n", temps)

# a) Task: Calculate the average temperature for each city (row-wise)
avg_temp_per_city = np.mean(temps, axis=1)
print("\nAverage temperature for each city:\n", avg_temp_per_city)

# b) Task: Find the hottest day for each city (maximum temperature)
max_temp_per_city = np.max(temps, axis=1)
print("\nHottest day (temperature) for each city:\n", max_temp_per_city)

# c) Task: Find the overall highest temperature recorded
overall_max_temp = np.max(temps)
print("\nOverall highest temperature recorded:\n", overall_max_temp)

# d) Task: Calculate temperature deviations from the mean for each city
# Subtract each city's mean from its daily temperatures (broadcasting)
deviations = temps - avg_temp_per_city[:, np.newaxis]
print("\nTemperature deviations from the mean for each city:\n", deviations)

# e) Task: Identify cities with consistent temperatures (std dev < 3°C)
std_devs = np.std(temps, axis=1)
consistent_cities = np.where(std_devs < 3)[0]
print("\nCities with consistent temperatures (std dev < 3°C):\n", consistent_cities)
