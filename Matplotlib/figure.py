import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 10)
y = x ** 2

fig = plt.figure(figsize=(10, 6), dpi=70)  # Create a figure with specified size and resolution

axis1 = fig.add_axes([0.1, 0.1, 0.7, 0.8])  # Add the first axis to the figure [left, bottom, width, height]
# left   = distance from left edge
# bottom = distance from bottom edge
# width  = width of graph
# height = height of graph
axis1.plot(x, y)  # Plot on the first axis

axis2 = fig.add_axes([0.55, 0.1, 0.35, 0.6])  # Add the second axis to the figure
axis2.plot(x, y)  # Plot on the second axis

plt.scatter(x, y)  # Add a scatter plot to the figure
plt.savefig("basicplot.png")  # Save the figure

plt.show()  # Display the figure with both axes



