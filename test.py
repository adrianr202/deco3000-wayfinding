import matplotlib.pyplot as plt
import numpy as np

# Your array of numbers
y = [56, 59, 60, 64, 64, 66, 68, 69, 70, 70, 72, 72, 75, 76, 77, 77, 79, 79, 80, 81, 82, 83, 83, 84, 84, 84, 87]
x = [2.33, 2.93, 3.16, 4.3, 4.3, 5.01, 5.84, 6.31, 6.81, 6.81, 7.94, 7.94, 10.0, 10.8, 11.66, 11.66, 13.59, 13.59, 14.68, 15.85, 17.11, 18.48, 18.48, 19.95, 19.95, 19.95, 25.12]

# Create a scatter plotc
plt.scatter(x, y, marker='o', color='blue')

# Set the labels for the axes
plt.xlabel('Est. Distance (m)')
plt.ylabel('Signal Strength (Dbm)')

# Display the plot
plt.show()