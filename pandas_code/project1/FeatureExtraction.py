import numpy as np
import pandas as pd
from dateutil.relativedelta import relativedelta
from datetime import datetime

df = pd.read_csv(r'pandas_code/project1/anime.csv')

print(df.head())
print("\n \n")

#This is used to get the column names of the dataframe
print(df.loc[4]['Title'])

#This function is used to extract the episode number from the title of the anime. It looks for the text within parentheses and returns it as a string. If there are no parentheses, it returns an empty string.
def extract_episode(txt):
    check = False
    data = "" 
    for i in txt:
        if i == ')':
            check = False
            break
        if check == True:
            data = data + i
        if i == '(':
            check = True
    return data


# Extract episodes from titles
df["Episodes"] = df["Title"].apply(extract_episode)
print(df.head())
print("\n \n")

# Remove the " eps" suffix from the Episodes column
df["Episodes"] = df["Episodes"].str.replace(" eps", "")
print(df.head())
print("\n \n")


# Convert the Episodes column to integer type
df['Episodes'] = df['Episodes'].astype(int)
print(df.head())
print("\n \n")


#make a new column for time stamp

def extract_time(txt):
    check = False
    data1 = ""

    for i in range(len(txt)):
        if txt[i] == ')':
            for j in range(i+1,i+20):
                  data1 += txt[j]
    return data1.strip()
          

# Extract time from titles
df["Time"] = df["Title"].apply(extract_time)
print(df.head())
print("\n \n")


# This function is used to extract the total time from the Time column. It looks for the text within parentheses and returns it as a string. If there are no parentheses, it returns an empty string.
def calculate_total_months(period):
    try:
        start_str, end_str = period.split(' - ')
        start_date = datetime.strptime(start_str, '%b %Y')
        end_date = datetime.strptime(end_str, '%b %Y')
        r = relativedelta(end_date, start_date)
        return r.years * 12 + r.months + 1  # +1 to include the starting month
    except:
        return None
    
# Calculate total months and add as a new column
df['Months'] = df['Time'].apply(calculate_total_months)
print(df.head())
print("\n \n")

# This function is used to extract the total time from the Time column. It looks for the text within parentheses and returns it as a string. If there are no parentheses, it returns an empty string.
df[df['Score'] == df['Score'].max()]['Title']
print(df['Title'].head())
print("\n \n")

