import numpy as np
import pandas as pd

df = pd.read_csv('Production.csv')
print(df)

print("=============")

# find minimum value of produaction and print it 
mini = df['Production'].min()
print("Minimum value : " ,mini)

print("======================")

# print the Mine Name whose Production is equal to 0

name = (df.loc[(df["Production"] == 0)])
print(name.iloc[:,2:3])
print("================")

# find second highestProduction
sec = sorted(df['Production'])[-2]
print("Second Highest value :",sec)

# third minimum labour hours
third = sorted(df['Labor_Hours'])[3]
print("Third minimum labor hours value :",third)


# Using describe 
report = df["Labor_Hours"].describe()
print(report)
df.to_csv('pro_result.csv')


print("====================================================================================")

# • Insert a column at the last position in the csv sheet and fill it with NaN values.

df['new_col'] = pd.Series([np.NaN])
print(df) 
df.to_csv('pro_result.csv')

print("====================================================================================")

# •calculate sum and average labour hour

pro_sum = df["Production"].sum()
print("Total Production : ",pro_sum)

labor_hours = df["Labor_Hours"].sum()
print("Total Labor Hours : ",labor_hours)

print("====================================================================================")

# • Store the updated csv file as result.csv.






