

import numpy as np
import pandas as pd


def pr(df):
    print(df['Production'])
    if (df['Production'] == '0'):
        print(df['Mine_Name'])


df = pd.read_csv('Production.csv')


print(min(df['Production']))
print(max(df['Production']))
print("------------------------")
mine = (df.loc[(df['Production'] == 0)])
print(mine.iloc[:, 2:3])

print(df.nlargest(2, 'Production'))

lh=df.nlargest(3, 'Labor_Hours')


