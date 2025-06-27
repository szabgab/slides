import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)


planet_selector = df['Planet name'].isin(['Earth', 'Mars'])
print(planet_selector)
print()

planets = df[ planet_selector ]
print(planets)
