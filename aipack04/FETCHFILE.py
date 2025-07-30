import pandas as pd

restore_sheet = pd.read_excel('Cvent_List of Intrerested Students_CR(2).xlsx',
                              sheet_name='Student list',
                              index_col=None,
                              na_values=['NA'])

print(restore_sheet)