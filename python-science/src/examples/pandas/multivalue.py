import pandas as pd

df = pd.read_csv('multivalue.csv')
print(df)
print()

values = ["Apple", "Banana", "Peach", "Melon"]
for value in values:
    df[value] = df.apply(lambda row: pd.notnull(row['Fruits']) and value in row['Fruits'].split(','), axis=1)

print( df )
