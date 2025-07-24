import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)


big_ones_selector = df['Mass'] > 1
print(big_ones_selector)
print()

big_ones = df[big_ones_selector]
print(big_ones)
