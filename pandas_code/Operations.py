import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
})

print(df1.shape) # (5, 3)
print("Size of DataFrame:", df1.size) # 15
print("\n \n")

print("DataFrame Info:")
print(df1.info())
print("\n \n")

print("DataFrame Description:")
print(df1.describe())
print("\n \n")

sum = df1['A'] + 10
print(sum)
print("\n \n")

# Applying a function to a column
def square(x):
    return x ** 2


df1['A_squared'] = df1['A'].apply(square)
print(df1)







