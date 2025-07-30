import numpy as np
import pandas as pd


df = pd.DataFrame(
    np.random.randn(6, 4),
    index=pd.date_range(start='20190101', periods=6, freq='D'),
    columns=['A', 'B', 'C', 'D']
)

print("\n\n")
print(df.loc['2019-01-06'])
dates = pd.date_range(start='20190101', periods=6, freq='D')
print(df.loc[dates[0]])
print("\n\n")
print(df.loc[: , ['A','D']])
print("\n\n")
print(df.loc['2019-01-04' , ['A','D']])