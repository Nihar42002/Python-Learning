import pandas as pd
# list1 = [[1, 2, 3, 4, 5] , ['a', 'b', 'c', 'd', 'e']]
# print(list1)

# df = pd.DataFrame(list1,columns=["h","b","l","g","y"])
# print(df)

df = pd.read_csv("./Iris.csv")
# print(df.iloc[7:10][["Id","Species"]])
print(df[df["Species"]!="Iris-virginica"])
print(df.head())