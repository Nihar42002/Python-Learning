import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)

# Group by Category and calculate the sum of Sales
cat = df.groupby('Category')['Sales'].sum()
print(cat)
print("\n \n")



# Group by Store and calculate the sum of Sales
cat1 = df.groupby('Store')['Sales'].sum()
print(cat1)
print("\n \n")



# Group by multiple columns
# Group by Category and Store
cat3 = df.groupby(['Category','Store'])['Sales'].sum()
print(cat3)
print("\n \n")


print("Mean:", df['Sales'].mean())
print("Median:", df['Sales'].median())
print("Min:", df['Sales'].min())
print("Max:", df['Sales'].max())
print("Count:", df['Sales'].count())
print("Std:", df['Sales'].std())
print("\n \n")

print(df['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median']))
