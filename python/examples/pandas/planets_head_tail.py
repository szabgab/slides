import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)
print(df.head())

print()
print(df.tail(2))
