import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

print(df.columns)
print()

print(df.dtypes)
print()

print(df.index)
print()

print(df.values)
print()

print(df.describe())

