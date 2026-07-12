import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#basic linear space graph

x = np.linspace(0, 6, 10)
y = x ** 2
plt.plot(x, y)
plt.title("Basic Linear Space Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")


