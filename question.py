"""Write a python script that loads the “Marks.csv” file and do the following:
1. Add the “Total” column, which stores the total of all the subject marks.
2. Add columns FOP_GRADES, DBMS_GRADES, CFO_GRADES, MATHS_GRADES, and PC_GRADES. These columns store the grades scored by the student based on subject marks. Grades calculated based on the given criteria:
• If the subject marks less than 40, then the grade is FF.
• If the subject marks between 40 to 50, then the grade is CC.
• If the subject marks between 50 to 60, then the grade is BC.
• If the subject marks between 60 to 70, then the grade is AB.
• If the subject marks greater than 70, then the grade is AA.
3. Add the “Percentage” column, which stores the percentage.
4. Add the “Result Class” column, which stores the result of the student. The result will be considered based on the given criteria:
• If the student scores less than 40 marks in any subject or the percentage is less than 40, store the result “FAIL”.
• If the percentage is between 40 to 50, then store result “PASS”.
• If the percentage is between 50 to 60, then store result “SECOND”.
• If the percentage is between 60 to 70, then store result “FIRST”.
• If the percentage is greater than 70, then store result “DISTINCTION”.
5. Print the name of the student who secured the 1st Rank based on percentage.
6. Print the name of the student who secured the minimum percentage.
7. Store the updated csv file as result.csv.
[20]
Marks :
"""

# python exam question 
import numpy as np
import pandas as pd


def percentage(obj):
   
    if (obj<= 40):
        return "FF"
    elif (obj>40 and obj<50):
        return 'CC'
    elif (obj>50 and obj<60):
        return 'BC'
    elif (obj>60 and obj<70):
        return 'AB'
    elif (obj>40):
        return 'AA'
    
def percentageclass(df):
    if (df['percetnage']<= 40):
        return "FAIL"
    elif (df['percetnage']>40 and df['percetnage']<50):
        return 'PASS'
    elif (df['percetnage']>50 and df['percetnage']<60):
        return 'SECOND'
    elif (df['percetnage']>60 and df['percetnage']<70):
        return 'FIRST'
    elif (df['percetnage']>40):
        return 'DISTINCTION'

df = pd.read_csv('Marks.csv')

print(df)
#Add Total Colun at the end 
df['total'] = df['FOP']+df['DBMS']+df['CFO']+df['MATHS']+df['PC']
print(df)


# Calculate for all subject weather student is pass in every subject or not 
df['FOP_GRADS'] = df['FOP'].apply(percentage)
df['DBMS_GRADS'] = df['DBMS'].apply(percentage)
df['CFO_GRADS'] = df['CFO'].apply(percentage)
df['MATHS_GRADS'] = df['MATHS'].apply(percentage)
df['PC_GRADS'] = df['PC'].apply(percentage)


# find the percentage of all student
df['percetnage']=(df['total'])*100/500

df['result'] =df.apply(percentageclass,axis=1)


# print(df)
vr=df.nlargest(1,'percetnage')
print(vr)

df.to_csv('result.csv',index=False)

