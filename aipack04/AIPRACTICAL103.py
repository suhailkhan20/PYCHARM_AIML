import pandas as pd
import numpy as np

print("numpy matrix = \n\n", np.random.randn(6,4))

df = pd.DataFrame(np.random.randn(6,4),
                  index = pd.date_range('20190101', periods=6, freq='D'),
                  columns = ['A','B','C','D'] )

print("\n\nPandas Dataframe = \n", df)
print("\n\nPandas Columns= \n", df.columns)
print("\n\nPandas Index = \n", df.index)
print("\n\nPandas Values = \n", df.values)
