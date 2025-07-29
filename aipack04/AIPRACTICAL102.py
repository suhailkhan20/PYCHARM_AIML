import pandas as pd
dates = pd.date_range(start='20250701', periods=6, freq="YE")
print(dates)

print('dates[0]',dates[0])