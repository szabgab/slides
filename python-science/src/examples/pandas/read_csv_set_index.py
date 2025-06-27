import pandas as pd

df = pd.read_csv('planets.csv', index_col='Planet name')
print(df.head(2))
