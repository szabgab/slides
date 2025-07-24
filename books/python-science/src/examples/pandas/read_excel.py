import sys
import pandas as pd

if len(sys.argv) < 2:
    exit("Need filename")
filename = sys.argv[1]

df = pd.read_excel(filename)
print(df)

# to_excel()
