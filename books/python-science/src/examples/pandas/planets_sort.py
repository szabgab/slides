import sys
import pandas as pd

filename = "planets.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

sorted_df = df.sort_values('Planet name', ascending=True)
print(sorted_df)
# df remains unchanged
