import pandas as pd
df1= pd.read_csv("tested.csv")
print(df1)
print(df1.head(2))

#sorting columns by Name
print("DataFrame after sorting by Name")
print(df1.sort_values("Name"))

