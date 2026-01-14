import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sugarcane dataset
df = pd.read_csv('List of Countries by Sugarcane Production.csv')

print(df.head())
print(df.shape)
print(df.info())

# Data Cleaning
df['Production(Tons)'] = df['Production(Tons)'].str.replace(',', '')
df["Production per Person (Kg)"] = df["Production per Person (Kg)"].str.replace(".","").str.replace(",",".")
df["Acreage (Hectare)"] = df["Acreage (Hectare)"].str.replace(".","")
df["Yield (Kg / Hectare)"]= df["Yield (Kg / Hectare)"].str.replace(".","").str.replace(",",".")

df = df.drop( "Unnamed: 0", axis = 1)

df.rename(columns= {"Production (Tons)": "Production(Tons)"}, inplace = True)
df.rename(columns= {"Production per Person (Kg)": "Production_per_person(Kg)"}, inplace = True)
df.rename(columns= {"Acreage (Hectare)": "Acreage(Hectare)"}, inplace = True)
df.rename(columns= {"Yield (Kg / Hectare)": "Yield(Kg/Hectare)"}, inplace = True)

df.isna().sum()
df[df["Acreage(Hectare)"].isnull()]
df = df.dropna().reset_index().drop("index", axis = 1)
print(df)

print(df.nunique())
print(df.dtypes)

df["Production(Tons)"] = df["Production(Tons)"].astype(float)
df["Production_per_person(Kg)"] = df["Production_per_person(Kg)"].astype(float)
df["Acreage(Hectare)"] = df["Acreage(Hectare)"].astype(float)
df["Yield(Kg/Hectare)"] = df["Yield(Kg/Hectare)"].astype(float)
print(df.dtypes)

# Univariate Analysis
df.head()

#How many countries produce sugarcane from each continent?
df["Continent"].value_counts()
df["Continent"].value_counts().plot(kind = "bar")
df.describe()

#Checking outliers

plt.figure(figsize = (10,8))
plt.subplot(2,2,1)
sns.boxplot(df["Production(Tons)"])
plt.title("Production(Tons)")
plt.subplot(2,2,2)
sns.boxplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")
plt.subplot(2,2,3)
sns.boxplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")
plt.subplot(2,2,4)
sns.boxplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")
plt.show()

#Distribution of the columns
plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
sns.distplot(df["Production(Tons)"])
plt.title("Production(Tons)")
plt.subplot(2,2,2)
sns.distplot(df["Production_per_person(Kg)"])
plt.title("Production_per_person(Kg)")
plt.subplot(2,2,3)
sns.distplot(df["Acreage(Hectare)"])
plt.title("Acreage(Hectare)")
plt.subplot(2,2,4)
sns.distplot(df["Yield(Kg/Hectare)"])
plt.title("Yield(Kg/Hectare)")
plt.show()

sns.violinplot(df["Production(Tons)"])

#Bivariate Analysis
# Which country produces maximum sugarcane?
df_new = df[["Country","Production(Tons)"]].set_index("Country")
print(df_new)

df_new["Production(Tons)_percent"] = df_new["Production(Tons)"]*100/df_new["Production(Tons)"].sum()
print(df_new)

df_new["Production(Tons)_percent"].plot(kind = "pie", autopct = "%.2f")
df[["Country","Production(Tons)"]].set_index("Country").sort_values("Production(Tons)", ascending = False).head(15).plot(kind = "bar")

ax = sns.barplot(data = df.head(15),  x= "Country", y = "Production(Tons)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()

#Which country has highest land?
df_acr = df.sort_values("Acreage(Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_acr,  x= "Country", y = "Acreage(Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()

#Which country has highest yield per hectare?
df_yield = df.sort_values("Yield(Kg/Hectare)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Yield(Kg/Hectare)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()

#Which country has highest production?
df_yield = df.sort_values("Production_per_person(Kg)", ascending = False).head(15)
ax = sns.barplot(data = df_yield,  x= "Country", y = "Production_per_person(Kg)")
ax.set_xticklabels(ax.get_xticklabels(),rotation =90)
plt.show()

#Correlation
print(df.corr())
sns.heatmap(df.corr(), annot = True, cmap="Greens")

#Do countries with highest land produce more sugarcane?
sns.scatterplot(data = df, x = "Acreage(Hectare)", y = "Production(Tons)", hue = "Continent" )

#Do countries which yield more sugarcane per hectare produces more sugarcane in total?
sns.scatterplot(data = df, x = "Yield(Kg/Hectare)" , y = "Production(Tons)", hue = "Continent")

#Analysis for Continent
df_continent = df.groupby("Continent").sum()
df_continent["number_of_countries"] = df.groupby("Continent").count()["Country"]
print(df_continent)

#Which continent produces maximum sugarcane?
df_continent["Production(Tons)"].sort_values(ascending =  False).plot(kind = "bar")

#Do number of countries in a Continent effects production of sugarcane?
continent_names = df_continent.index.to_list()
sns.lineplot(data = df_continent,x = "number_of_countries", y= "Production(Tons)" )
plt.xticks(df_continent["number_of_countries"], continent_names, rotation =90)
plt.show()

#Do continent with highest land produces more sugarcane?
sns.lineplot(data = df_continent,x = "Acreage(Hectare)", y= "Production(Tons)" )

#Production distribution by continent
df_continent["Production(Tons)"].plot(kind = "pie", autopct = "%.2f%%")
plt.title('Production Distribution by Continent')
plt.show()

#Correlation for continent
print(df_continent.corr())
