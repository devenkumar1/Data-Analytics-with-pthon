import pandas as pd
data= pd.read_csv("Book1.csv")
print(data)
#printing first 2 rows
print(data.head(2))


print("printing row 1")
row1=data.loc[1]
print(row1)
print("")
#applying condition in data frame
print("applying condition age>30 in data frame")
print(data[data["age"]>30])

#condition to list student pursuing MCA
print("students pursuing MCA")
mca_students= data.loc[data['programme'] == 'MCA']
print(mca_students)
  
#save mc_students to csv file

mca_students.to_csv("mca_students.csv")



#skip first 3 rows.
# print("after skipping first three rows")
# df2=pd.read_csv("Book1.csv",skiprows=3)
# print(df2)

#print(data.head(2))
#sort by name
# print("DataFrame after sorting by Name")
# print(data.sort_values("name"))


#for skipping column name:
# df3=pd.read_csv("Book1.csv",index_col="name")
# print(df3)
# print(df2["name"])

#print row 1

