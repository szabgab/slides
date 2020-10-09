import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

print(df['Mass'])
print()

print(df['Planet name'])
print()

print(df[2:5]) # using row numbers (just like iloc)
print()

print(df.iloc[3:6][['Distance (AU)', 'Planet name']])
print()

