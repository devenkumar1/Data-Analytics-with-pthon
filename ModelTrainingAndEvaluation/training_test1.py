import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df = pd.read_csv("titanic.csv")
print(df)

# Map 'passengerClass' to numerical values
df['passengerClass'] = df['passengerClass'].map({'1st': 1, '2nd': 2, '3rd': 3})

# Convert 'sex' to numeric (0 = female, 1 = male)
df['sex'] = df['sex'].map({'female': 0, 'male': 1})

# Convert 'survived' to numeric (1 = yes, 0 = no)
df['survived'] = df['survived'].map({'yes': 1, 'no': 0})

# Select features
x = df[["age", "passengerClass", "sex"]]  # Corrected this line
y = df["survived"]

# Handle missing values
x.fillna(x.mean(), inplace=True)

# Handling missing values in y, assuming that 'y' is binary (survived or not)
y.fillna(y.mode()[0], inplace=True)  # Replacing NaNs in 'y' with the most frequent value (mode)

# Split the data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Linear regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Get the coefficients and intercept
coefficients = model.coef_
intercept = model.intercept_

# Print the equation
print('Equation:')
print("Survived =", intercept, end=" ")
for i, coefficient in enumerate(coefficients):
    print(f"{coefficient} * {x.columns[i]}", end=" ")
    print(" + " if i < len(coefficients) - 1 else "")
print()

# Get the predictions
y_pred = model.predict(x_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
