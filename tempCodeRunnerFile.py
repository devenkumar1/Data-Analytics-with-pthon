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