import pandas as pd
import numpy as np

df = pd.read_csv('mixed.csv', dtype = { 'MyInteger' : np.int8 })
print( df.dtypes )

