import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4),
                  index=pd.date_range('20190101',periods=6,freq='D'),
                  columns=['A','B','C','D'])
print("df =",df)
print("\ndf.A=",df.A)
print("\ndf[df.A >0] =")
print(df[df.A >=0])

print("\n\n")
print(df[(df.A < 0) & (df.B < 0)])
print("\n\n")
print(df[df.A >=0])
