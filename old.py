import numpy as np
import pandas as pd


def percentage(df):
    if (df['Percentage'] < 40):
        return "FF"
    elif (df['Percentage'] >= 40 and df['Percentage'] < 50):
        return "cc"
    elif (df['Percentage'] >= 50 and df['Percentage'] < 60):
        return "BC"
    else:
        return "AB"


df = pd.read_csv('data.csv')

print(df)
print()
print('========')

df['total'] = df['q1']+df['q2']+df['q3']
df['Percentage'] = (df['total'])*100/30
df['result'] = df.apply(percentage, axis=1)
print(df)

df.to_csv('temp.csv')

df = pd.read_csv('temp.csv')
