import pandas as pd

df = pd.read_csv('BlackFriday.csv')

del df['Product_Category_2']
del df['Product_Category_3']

print(df.head())

df['User_ID'].nunique()

df['Product_ID'].nunique()

df['Gender'].unique()

df['Age'].unique()

df['Occupation'].unique()

df['City_Category'].unique()

df['Stay_In_Current_City_Years'].unique()

df['Marital_Status'].unique()

df['Product_Category_1'].unique()

df['Purchase'].sum()/len(df['Purchase'])

for column in df.columns:
    print(column, ":" ,df[column].nunique())
