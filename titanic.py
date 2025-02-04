import pandas as pd
import matplotlib.pyplot as plt
titanic=pd.read_csv("titanic.csv")

# print(titanic.head())


print("shape before deleting duplicate values",titanic.shape)

titanicData=titanic.drop_duplicates()
print("Shape after deleting the duplicate values",titanicData.shape)

#checking null values in the dataset
titanicNull=titanic.isnull().sum()
print(titanicNull)


# #dropping null values
# titanicData=titanic.dropna()
# print("shape after dropping null values",titanicData.shape)
print("info:")
print(titanic.info)

#describe command
print("describe:")
print(titanic.describe(include="all"))

#unique command
print("unique:")
print(titanic.nunique())
#delete columns
print("delete columns:")
titanicData=titanic.drop("survived",axis=1)
print(titanicData.head())

#plot using seaborn
# import seaborn as sns
# sns.set_style("whitegrid")
# sns.countplot(x="sex",data=titanic, hue="survived")
# plt.show()

# #histogram age distribution by gender
# data = sns.load_dataset("titanic")
# plt.figure(figsize=(10, 6))
# sns.histplot(data=data, x="age", kde=True,hue='sex')
# plt.title('Age Distribution by Gender')
# plt.show()

# #barplot survival rate by passenger class and gender

# #a histogram using pl  
# plt.title("Age Distribution")
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.hist(titanic["age"],color="#69b3a2")
# plt.show()


#pie chart
# plt.title("Survival Rate by Gender")
# labels = titanic['sex'].unique()
# myexplode=[0.2,0.8]
# plt.pie(titanic['sex'].value_counts(), labels = labels, autopct='%1.1f%%',explode=myexplode)
# plt.show()

# t1= titanic[(titanic["passengerClass"]>1) & (titanic["passengerClass"]<3)]
# print(t1)

titanic.drop(titanic.head(10).index,inplace=True)
print(titanic)


age_count=titanic["age"].value_counts()
print(age_count)
plt.pie(age_count,labels=age_count.index)
plt.show()


import sklearn as skl 
from sklearn.model_selection import train_test_split

X=titanic.drop("survived",axis=1)
y=titanic["survived"]

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#linear regression
