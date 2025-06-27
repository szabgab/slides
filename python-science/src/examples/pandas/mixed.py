import pandas as pd

df = pd.read_csv('mixed.csv')
print( df.dtypes )
print( df.describe() )

