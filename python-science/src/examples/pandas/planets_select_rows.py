import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

rows = df[2:5] # using row numbers
print(type(rows))
print(rows)
print()

iloc_rows = df.iloc[2:5] # just like plain []
print(type(iloc_rows))
print(iloc_rows)
print()

picked_rows = df.iloc[[2,5,3]] # using specific row numbers
print(type(picked_rows))
print(picked_rows)
print()
# df[[2,5,3]] would not work so we need iloc

