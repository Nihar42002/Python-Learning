
import pandas as pd
df = pd.read_csv("./work_from_home_burnout_dataset.csv")

pd.set_option("display.max_rows", None) # to display all rows in the dataframe
pd.set_option("display.max_columns", None) # to display all columns in the dataframe
print(df.columns) # to display the column names of the dataframe
print(df.loc[df["burnout_risk"]=="Low"])

# print(df.head()) # prints the first 5 rows of the dataframe
# print(df.tail()) # prints the last 5 rows of the dataframe
# print(pd.options.display.max_rows) 
# print(df.info())# prints the summary of the dataframe
