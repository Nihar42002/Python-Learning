import numpy as np
import pandas as pd

data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary',
            'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)

df['Month'] = df['Date'].dt.month_name() # to extract the month name from the date column
df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)

print(df)
print("\n \n")


print("Pivot Table: Total Sales by Product and Region")
print(pd.pivot_table(df, values='Sales', index='Region', columns='Product'))
print("\n \n")


print("Pivot Table: Total Sales by Product and Region with Aggregation")
pd.pivot_table(df,values = "Sales",index = 'Region',columns="Product",aggfunc = 'median')
print("\n \n")

print("Pivot Table: Total Sales and Units by Product and Region")
pivot2 = pd.pivot_table(df, values=['Sales', 'Units'], index='Region', columns='Product')
print(pivot2)
print("\n \n")

print("Crosstab: Sales by Region and Product")
print(pd.crosstab(df['Region'], df['Product']))
