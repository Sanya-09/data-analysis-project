import pandas as pd
df = pd.read_csv('BlackFriday.csv')
print(df.head())
print(df.info())
print(df)
print(df.isnull().sum())
print(df.dropna())
del df['Product_Category_2']
del df['Product_Category_3']
print(df)
