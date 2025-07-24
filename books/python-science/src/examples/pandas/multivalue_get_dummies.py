import pandas as pd

dfin = pd.read_csv('multivalue.csv')
print(dfin)
print()
fruits_dummies = dfin['Fruits'].str.get_dummies(',').astype(bool)
df = pd.concat([dfin, fruits_dummies], axis=1)
print(df)

