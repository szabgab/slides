import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

selector = (df['Mass'] > 1) & (df['Mass'] < 100)
print(selector)
print()

planets = df[ selector ]
print(planets)
