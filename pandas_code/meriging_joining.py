import numpy as np
import pandas as pd

#first dataframe
dict_orders = pd.DataFrame({
"id": [1, 2, 3, 6, 7 ],
"name": ["Alice", "Nihar", "Carla", "David", "Eva"],
"product": ["Notebook", "Pen", "sticker", "Notebook", "Marker"],
"quantity": [2, 10, 1, 3, 4],
"price_usd": [4.50, 1.50, 12.00, 4.50, 1.75],
"date": ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05"]
})

#second dataframe
dict_designations = pd.DataFrame({
"id": [1, 2, 3, 4, 5],
"designation": ["Manager", "Sales", "Designer", "Engineer", "Analyst"],
"department": ["Ops", "Sales", "Design", "Engineering", "Analytics"]
})

#merging the dataframes
print(pd.merge(dict_orders, dict_designations))
print("\n \n")

#merging the dataframes on the 'id' column
print(pd.merge(dict_orders, dict_designations, on='id'))
print("\n \n")

#merging the dataframes on the 'id' column with an inner join
print(pd.merge(dict_orders, dict_designations, on='id', how='inner'))
print("\n \n")

#merging the dataframes on the 'id' column with a outer join
print(pd.merge(dict_orders, dict_designations, on='id', how='outer'))
print("\n \n")

#merging the dataframes on the 'id' column with a left join
print(pd.merge(dict_orders, dict_designations, on='id', how='left'))
print("\n \n")

#merging the dataframes on the 'id' column with a right join
print(pd.merge(dict_orders, dict_designations, on='id', how='right'))
print("\n \n")

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2'],
    'C': ['C0', 'C1', 'C2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5'],
    'C': ['C3', 'C4', 'C5']
})

#concatenating the dataframes
print(pd.concat([df1, df2]))
print("\n \n")

#concatenating the dataframes along the columns
print(pd.concat([df1, df2], axis=1))
print("\n \n")

df3 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

# Second DataFrame
df4 = pd.DataFrame({
    'score': [85, 90, 75]
}, index=[2, 3, 4])

# Joining the DataFrames using the join() method
print(df3.join(df4, how='outer'))
print("\n \n")

# joining the dataframes
print(df4.join(df3))
