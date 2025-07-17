import pandas
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_column', None)
#pandas.set_option('display.width', 1000)

filename="C:\\Users\\suhai\\PycharmProjects\\MIS_DATA\\indians-diabetes.data.csv"

hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass',   'pedi', 'age', 'class']

df = pandas.read_csv(filename, names=hnames   )
print("Size of training data = ", df.shape)
print("\n\n", df.dtypes)
print("\n\n", df.columns )

print("\n\n",df)