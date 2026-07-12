import numpy as np
import pandas as pd


data = {
"id": [1, 2, 3, 4, 5],
"name": ["Alice", "Nihar", "Carla", "David", "Eva"],
"product": ["Notebook", "Pen", np.nan, "Notebook", "Marker"],
"quantity": [2, 10, 1, np.nan, 4],
"price_usd": [4.50, np.nan, 12.00, 4.50, 1.75],
"date": ["2026-06-01", "2026-06-02", np.nan, "2026-06-04", "2026-06-05"],
"designation": ["Manager", "Sales", np.nan, "Engineer", np.nan]
}

# Create a dataframe from the dictionary
df = pd.DataFrame(data)
print(df)
print("\n \n")

# Check for missing values in the dataframe
print(df.isna())
print("\n \n")

# Count the total number of missing values in each column
print(df.isna().sum())
print("\n \n")

# Check if there are any missing values in the dataframe
print(df.isna().any())
print("\n \n")

print(df.dropna()) # to drop the rows with missing values
print("\n \n")


print(df.dropna(thresh = 4))# to drop the rows with at least 4 non-missing values
print("\n \n")

print(df.dropna(subset=["product", "quantity"])) # to drop the rows with missing values in the specified columns
print("\n \n")

print(df.fillna(0)) # to fill the missing values with a specified value
print("\n \n")

values = {"product": "Unknown", "quantity": 0, "price_usd": 0.0, "date": "Unknown", "designation": "Unknown"}
print(df.fillna(value=values)) # to fill the missing values with a specified value for each column
print("\n \n")


#If we want to use the mean of the column use a different data which has numeric values in the column:-
print(df.fillna(df.mean()))# to fill the missing values with the mean of the column (only for numeric columns)
print("\n \n")