import pandas as pd
import  matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("tested.csv")

print(data)
print("head of the data:")
print(data.head())

print("tail of the data:")

print(data.tail())
print("")

#summary
print("summary of the data :")
print(data.describe())

print("after sorting")
print(data.sort_values("Age"))




