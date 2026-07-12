import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 10)
y = x ** 2

plt.subplot(2,2,1) # Create a 2x2 grid of subplots and select the first one
plt.plot(x, y)
plt.title("Subplot 1")
plt.xlabel("X Values")
plt.ylabel("Y Values")


plt.subplot(2,2,2) # Select the second subplot
plt.plot(x, y)
plt.title("Subplot 2")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

