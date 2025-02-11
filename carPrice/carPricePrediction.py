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

plt.bar(df['horsepower'],df['highwaympg'])
plt.title('horsepower vs highwaympg')
plt.xlabel('horsepower')
plt.ylabel('highwaympg')

plt.show()

#pie chart
import matplotlib.pyplot as plt

plt.pie(df['fueltype'].value_counts(), labels=df['fueltype'].value_counts().index)
plt.title('fueltype distribution')
plt.xlabel('fueltype')
plt.ylabel('count')

plt.show()


#histogram

plt.hist(df['horsepower'])
plt.title('horsepower distribution')
plt.xlabel('horsepower')

plt.show()

#line chart

plt.plot(df['citympg'],df['highwaympg'])
plt.title('citympg vs highwaympg')
plt.xlabel('citympg')
plt.ylabel('highwaympg')

plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

# Machine Learning: Linear Regression Model
x_train, x_test, y_train, y_test = train_test_split(df[['horsepower']], df[['highwaympg']], test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(x_train, y_train)

# Model coefficients and intercept
slope = model.coef_[0][0]
intercept = model.intercept_[0]

# Interpretation of the model
print(f"For every 1 unit increase in horsepower, highwaympg increases by {slope:.2f} units, on average, assuming all other variables are held constant.")
print(f"The intercept of the model is {intercept:.2f}, which means that if horsepower is 0, highwaympg is {intercept:.2f} units, on average.")


# Predictions and evaluation
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('Mean Squared Error:', mse)

#visualize the model
plt.scatter(x_test, y_test, color='blue')
plt.plot(x_test, y_pred, color='red')
plt.title('horsepower vs highwaympg')
plt.xlabel('horsepower')
plt.ylabel('highwaympg')
plt.show()

#number to float

# df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')

# #astype string
# df['seats']=df['seats'].astype(str)

#summarising and then visualising the graph

# df['seats'].value_counts().plot(kind='bar')
# #heading 
# plt.title('seats distribution')
# plt.xlabel('seats')
# plt.ylabel('count')

# plt.show()


#correlation heatmap

import seaborn as sns

sns.heatmap(df.corr(), annot=True)

plt.show()


