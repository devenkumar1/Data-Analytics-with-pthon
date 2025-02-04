import pandas as pd 
#data
data= [['Alex',10],['Bob',12],['Clarke',13],["John",14]]
#creating a dataframe
df=pd.DataFrame(data,columns=["Name","Age"])
print(df)


import pandas as pd
import numpy as np
data=[['cap1',20],['cap2',30],['cap3',40]]
df=pd.DataFrame(data,columns=['Course',"Marks"])
print(df)

#creating a dataframe from dictionary of lists

import pandas as pd
data={'Name':["name1","name2","name3","name4"],"Age":[28,34,29,42]}
df=pd.DataFrame(data)
print(df)

#creating a dataframe from list of dictionaries

import pandas as pd
data=[{'a':1,'b':2,"c":3,"d":4},{'a':5,'b':6,"c":7,"d":8}]
df=pd.DataFrame(data)
print(df)

#creating a dataframe from dict of series:
import pandas as pd

# Creating the DataFrame
info = {'one': pd.Series([1, 2, 3, 4, 5, 6], index=['a', 'b', 'c', 'd', 'e', 'f']),
        'two': pd.Series([7, 8, 9, 10, 11, 12], index=['a', 'b', 'c', 'd', 'e', 'f'])}

df = pd.DataFrame(info)
print("Original DataFrame:")
print(df)

# Add new column to an existing DataFrame by passing a series
print("\nAdd new column by passing series:")

df['three'] = pd.Series([20, 30, 60,70,80,90], index=["a", 'b', 'c',"d","e","f"])
print(df)

# Add new column using existing DataFrame
print("\nAdd new column using existing DataFrame:")

df["four"] = df["one"] + df["three"]
print(df)


#deleting columns from dataframe

print("delete the first column")
del df["one"]
print(df)


#creating indexed dataframe

import pandas as pd
data={"Name":["Tom","Jack","Steve","ricky"],"Age":[10,11,12,14]}

df= pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

print(df)

#row selection

print(df.loc['rank1'])


#addition of rows

import pandas as pd
data1={'Name':["tom","jack","steve","ricky"],"Age":[28,34,29,42]}
data2={'Name':'John',"Age":28}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2,index=[4])
print(pd.concat([df1, df2]))


#deleting rows from dataframe
import pandas as pd
data={'Name':["tom","jack","steve","ricky"],"Age":[28,34,29,42]}
df=pd.DataFrame(data)
print("Original DataFrame")
print(df)
print("DataFrame after deleting the first row")
df=df.drop(0)
print(df)

#sorting the dataframe

import pandas as pd
data={'Name':["tom","jack","steve","ricky"],"Age":[28,34,29,42]}
df=pd.DataFrame(data)
print("Original DataFrame")
print(df)
#sorting columns by Name
print("DataFrame after sorting by Name")
print(df.sort_values("Name"))

#descending order

print("DataFrame after sorting by Name in descending order")
print(df.sort_values("Name",ascending=False)) 



