import pandas as pd 

df = pd.read_csv('BlackFriday.csv')
del df['Product_Category_2']
del df['Product_Category_3']

df.head()

for column in df.columns:
    print(df[column].nunique(), "\t: ", column)

data = pd.DataFrame({'Ratio' : [len(df[df['Gender'] == 'M']), len(df[df['Gender'] == 'F'])]}, 
                    index = ['Male', 'Female'])

data.plot.pie(y = 'Ratio', figsize = (6,6), autopct = "%.1f")

df.groupby('Gender').size().plot(kind = 'pie', 
                                 autopct = "%.1f",
                                 title = 'Gender Ratio',
                                 figsize = (6,6))

df.groupby('Gender').size().plot(kind = 'bar', 
                                 figsize = (6,6))

df.groupby('Gender').size()

df.groupby('Gender').sum()['Purchase'].plot(kind = 'pie', autopct = "%0.1f")

df.groupby('Gender').mean()['Purchase'].plot(kind = 'pie', autopct = "%0.1f")
