from sklearn.model_selection import train_test_split
import pandas as pd

# population data
data = pd.DataFrame({
    'Age': [18, 22, 24, 30, 35, 40, 45, 50, 55, 60],
    'Group': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
})

# stratified sampling
stratifiedSampling = train_test_split(data, test_size=0.3, stratify=data['Group'], random_state=42)

print('stratifiedSampling:')
print(stratifiedSampling)
print("")
