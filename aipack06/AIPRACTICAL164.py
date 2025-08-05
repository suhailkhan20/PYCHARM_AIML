import warnings
warnings.filterwarnings(action='ignore')
# Correlations Matrix Plot
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', None)

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv('filepath_or_buffer', names=hnames)
correlations = dataframe.corr()