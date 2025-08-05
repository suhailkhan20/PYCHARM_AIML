import pandas as pd
import numpy as np
# dictionary of lists
dict = {'First Score' : [   100, 90, np.nan,     95 ],
        'Second Score': [    30, 45,     56, np.nan ],
        'Third Score' : [np.nan, 40,     80,     98 ]
       }

dict2 = np.random.rand(6,8)

# creating a dataframe from list
df = pd.DataFrame(dict)
df1 = pd.DataFrame(dict2)
print( df )

df2 = df.notnull()
print(df2)

print(df1)
df3 = df1.notnull()
print(df3)