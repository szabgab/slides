import pandas as pd

df = pd.read_csv('planets.csv')

print(df.head())
print()

df['dm'] = df['Distance (AU)'] * df['Mass']
print(df.head())
print()

df.drop(columns = 'Mass', inplace=True)
print(df.head())

