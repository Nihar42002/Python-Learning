import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import sample

data = sample(range(1, 100), 50)  # Generate a random sample of 50 numbers between 1 and 100
print(data)  # Print the generated data
plt.hist(data, bins=10 , edgecolor='black', linewidth=1.2)  # Create a histogram with 10 bins, black edges, and specified line width
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()

