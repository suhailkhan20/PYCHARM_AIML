import pandas as pd

url = 'https://github.com/suhailkhan20?tab=repositories'

data = pd.read_html(url)
print(data.head())