import pandas as pd
import numpy as np


other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)

# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
print(df.head(5))

print("The last 10 rows of the dataframe\n")
print(df.tail(10))
# =================================================================================

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
print(df.head(10))
# =================================================================================
# We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:
df1=df.replace('?',np.NaN)
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

print(df.columns)
# =================================================================================
# save .csv file

df.to_csv("automobile.csv", index=False)

# =================================================================================
# data types
print(df.dtypes)

# =================================================================================
#  to get a statistical summary
print(df.describe())
# describe all the columns in "df" 
print(df.describe(include = "all"))
print(df[['length', 'compression-ratio']].describe() )

# concise summary 
print(df.info())


