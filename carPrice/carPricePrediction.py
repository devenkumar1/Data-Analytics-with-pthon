import pandas as pd
import numpy as np

#load file
df=pd.read_csv('carData.csv')


print(df.columns)

print(df.count(0))

print(df.info)

print(df.isnull().sum())

print(df.describe())

print(df.dtypes)

print(df.shape)

print(df.index)

print(df.columns)

print(df.head(10))

print(df.tail(10))

#bar chart
import matplotlib.pyplot as plt

plt.bar(df['carbody'],df['price'])
plt.xlabel('CarName')
plt.ylabel('price')
plt.show()

