#importing pandas 
import pandas as pd
  
#reading a file
df= pd.read_csv("tested.csv")
#printing the data frame
print(df)
#printing first 10 rows
print(df.head(10))



#bokeh matplotlib  seaborn

import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y= np.array([3,8,1,10])

plt.bar(x,y)
plt.show()

