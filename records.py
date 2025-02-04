import pandas as pd
info={'one':pd.Series([10,20,30,40,50,60,70,80,90,100], index=['a','b','c','d','e','f','g','h','i','j']),
      'two':pd.Series([10,20,30,40,50,60,70,80,90,100], index=['a','b','c','d','e','f','g','h','i','j'])}

df=pd.DataFrame(info)
print(df)

pd.set_option("display.max_rows",None)