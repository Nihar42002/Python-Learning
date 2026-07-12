import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img  = mpimg.imread('Matplotlib/peak.jpg')  # Read an image file
plt.imshow(img) # Display the image
plt.axis('off') # Turn off the axis




cropped_img = img[50:200, 100:300]  # crop: rows 50-200, cols 100-300
plt.imshow(cropped_img)
plt.axis('off')
plt.show() # Show the image


