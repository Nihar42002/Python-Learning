import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

xaxis = np.linspace(0,5,11)

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(xaxis, xaxis+1, color="red", linewidth=0.25)
ax.plot(xaxis, xaxis+2, color="red", linewidth=0.50)
ax.plot(xaxis, xaxis+3, color="red", linewidth=1.00)
ax.plot(xaxis, xaxis+4, color="red", linewidth=2.00)

# possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
ax.plot(xaxis, xaxis+5, color="green", lw=3, linestyle='-')
ax.plot(xaxis, xaxis+6, color="green", lw=3, ls='-.')
ax.plot(xaxis, xaxis+7, color="green", lw=3, ls=':')

# custom dash
line, = ax.plot(xaxis, xaxis+8, color="black", lw=1.50)
line.set_dashes([5, 50, 15, 50]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(xaxis, xaxis+ 9, color="blue", lw=3, ls='-', marker='+') # Plot with a plus marker
ax.plot(xaxis, xaxis+10, color="blue", lw=3, ls='--', marker='o') # Plot with a circle marker
ax.plot(xaxis, xaxis+11, color="blue", lw=3, ls='-', marker='s') # Plot with a square marker
ax.plot(xaxis, xaxis+12, color="blue", lw=3, ls='--', marker='1') # Plot with a star marker
ax.plot(xaxis, xaxis+13, color="purple", lw=1, ls='-', marker='o', markersize=2) # Plot with a circle marker
ax.plot(xaxis, xaxis+14, color="purple", lw=1, ls='-', marker='o', markersize=4) # Plot with a circle marker
ax.plot(xaxis, xaxis+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red") # Plot with a circle marker
ax.plot(xaxis, xaxis+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=3, markeredgecolor="green"); # Plot with a square marker and custom edge color and width

plt.show()