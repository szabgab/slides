import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

# Load only data from a specific country.

country_name = 'Israel'
df = None
for chunk in pd.read_csv(filename, chunksize=10000):
    part = chunk[ chunk['Country'] == country_name ]
    if df is None:
        df = part.copy(deep = True)
    else:
        df = df.append(part.copy(deep = True), ignore_index = True)


print(df.count())
print(df.size)

