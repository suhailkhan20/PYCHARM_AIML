import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(6,4),
                  index=pd.date_range('20190101',periods=6,freq='D'),
                  columns=['A','B','C','D'])

print(df)

df.to_excel('outputData.xlsx',sheet_name='GNIOT')
print("Data saved in excel file.")