import pandas as pd
import numpy as np

print("numpy matrix = \n\n", np.random.randn(6,4))

df = pd.DataFrame(np.random.randn(6,4),
                  index = pd.date_range('20190101', periods=6, freq='D'),
                  columns = ['A','B','C','D'] )


print("Only one column access: ")
print(df.A)
print("\n\n")
print(df['B'])
print("\n\n")
print(df['D'])

print("\n\n")
print(df['2019-01-01' : '2019-01-03'])

print("\n\n")
print(df[0:3])

print("\n\n")
print(df['20190102':'20190104'])