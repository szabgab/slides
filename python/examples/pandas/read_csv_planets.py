import pandas as pd

df = pd.read_csv('planets.csv', index_col='name')
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
print(df)

df['dm'] = df['distance'] * df['mass']
print(df.head())

big = df[ df['mass'] > 20 ]
print(big)

