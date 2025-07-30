import numpy as np
import pandas as pd


df = pd.DataFrame(
    np.random.randn(6, 4),
    index=pd.date_range(start='20190101', periods=6, freq='D'),
    columns=['A', 'B', 'C', 'D']
)

print("\n\n")
print(df.iloc[3])

print("\n\n")
print(df.iloc[3:5, 0:2])