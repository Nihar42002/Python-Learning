import numpy as np
import pandas as pd

# Create a dataframe in the form of dictionary:-
data = [
{"id": 1, "name": "Alice", "product": "Notebook", "quantity": 2, "price_usd": 4.50, "date": "2026-06-01"},
{"id": 2, "name": "Bob", "product": "Pen", "quantity": 10, "price_usd": 0.99, "date": "2026-06-02"},
{"id": 3, "name": "Carla", "product": "Planner", "quantity": 1, "price_usd": 12.00, "date": "2026-06-03"},
{"id": 4, "name": "David", "product": "Notebook", "quantity": 3, "price_usd": 4.50, "date": "2026-06-04"},
{"id": 5, "name": "Eva", "product": "Marker", "quantity": 4, "price_usd": 1.75, "date": "2026-06-05"}
]

print(pd.DataFrame(data))

print("\n \n")

#Create a dataframe in the form of list:-
data_list = [
[1, "Alice", "Notebook", 2, 4.50, "2026-06-01"],
[2, "Bob", "Pen", 10, 0.99, "2026-06-02"],
[3, "Carla", "Planner", 1, 12.00, "2026-06-03"],
[4, "David", "Notebook", 3, 4.50, "2026-06-04"],
[5, "Eva", "Marker", 4, 1.75, "2026-06-05"]
]
print(pd.DataFrame(data_list))
print("\n \n")

columns = ["id", "name", "product", "quantity", "price_usd", "date"]
print(pd.DataFrame(data_list, columns=columns))
df2 = pd.DataFrame(data_list, columns=columns)
print("\n \n")

print(pd.DataFrame(data_list, columns=columns)[["name", "product"]])
print("\n \n")

df2["designation"] = ["Manager", "Sales", "Designer", "Engineer", "Analyst"]
print(df2)
print("\n \n")

# If we want to drop the column then we have to use drop() method:-
# comment out the inplace parameter because it will drop the column permanently and we want to show the dataframe after dropping the column:-
print(df2.drop("designation", axis=1))
print("\n \n")
print(df2.drop(0, axis=0)) # to drop the row with index 0
print("\n \n")

# If we want to drop the column permanently then we have to use inplace=True:-
print(df2.drop("designation", axis=1, inplace=True))
print(df2)
print("\n \n")

print(df2.loc[[1,2]]) # to access the element at row index 1 and column index 2
print("\n \n")

print(df2.iloc[[2,3]]) # to access the element at row index 2 and column index 3
print("\n \n")

print(df2.iloc[[2,3]] [["name", "product"]]) # to access the element at row index 2 and column index 3 and column name and product
print("\n \n")

print(df2[df2["quantity"] > 2]) # to access the element where quantity is greater than 2
print("\n \n")

print(df2[(df2["quantity"] > 2) & (df2["name"]=="Bob")]) # to access the element where quantity is greater than 2 and name is Bob
print("\n \n")




