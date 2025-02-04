import pandas as pd
import numpy as np


df = pd.read_csv('CarData.csv')

print(df)

#shape

df.fillna(0,inplace=True)

# print(df.isnull().sum())

print(df.shape)


#all unique carName
print(df['CarName'].unique())

#head
print("printing the head of the data frame")
print(df.head())

#regression analysis
 