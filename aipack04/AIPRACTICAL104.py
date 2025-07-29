import pandas as pd
import numpy as np

print("numpy matrix = \n\n", np.random.randn(6,4))

df = pd.DataFrame(np.random.randn(6,4),
                  index = pd.date_range('20190101', periods=6, freq='D'),
                  columns = ['A','B','C','D'] )

df['E'] = df['A'].apply(lambda y : 1 if(y>=0) else 0)
df['F'] = df['B'].apply(lambda y : "PASS" if y>= 0 else "FAIL")
print(df)

print("\n\n")
print(df.groupby('E').size())
print(df.groupby('F').size())

print("df.describe()", df.describe())
print("df.describe include all = \n", df.describe(include='all'))