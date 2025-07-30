import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4),
                  index=pd.date_range('20190101',periods=6,freq='D'),
                  columns=['A','B','C','D'])

print(df)

print("Mean \n\n")
print(df.mean())

print("only mean of B \n\n",df.B.mean())
print("only mean of B \n\n",df['B'].mean())

print("mean of row vise : ",df.mean(axis=1))