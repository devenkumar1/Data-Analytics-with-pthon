import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('healthcare.csv')

# Check the structure of the dataframe (optional)
print(df.head())  # this will help you verify if the columns are correct

# Calculate the correlation between 'Green_Vegetables_Consumption' and 'Age'
corr_matrix = df[["Green_Vegetables_Consumption", "Age"]].corr()
print(corr_matrix)

# Visualize the correlation matrix using a heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title('Correlation between Green Vegetables Consumption and Age')
plt.show()

# Get the absolute correlation values of all columns
correlation_with_target = df.corr().abs()

# Sort the correlations in descending order and get the top 10 features (excluding the target column itself)
top_k = correlation_with_target['Green_Vegetables_Consumption'].sort_values(ascending=False).head(11).index  # includes the target itself

# Exclude 'Green_Vegetables_Consumption' from the list to get the other features
top_k = top_k[top_k != 'Green_Vegetables_Consumption']

# Select the top 10 features
selected_features = df[top_k]

# Print the selected features (top 10 correlated with 'Green_Vegetables_Consumption')
print(selected_features)
