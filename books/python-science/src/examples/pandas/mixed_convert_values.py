import pandas as pd
import numpy as np

df = pd.read_csv('mixed.csv', converters = { 'MyExit' : lambda x : x == '0' })
print( df.dtypes )
print( df )
