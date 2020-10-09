import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

# Load only data from a specific country.

country_name = 'Israel'
chunks = []

for chunk in pd.read_csv(filename, chunksize=10000):
    print(chunk.size)
    part = chunk[ chunk['Country'] == country_name ]
    print(part.size)
    print('--')
    chunks.append(part)

df = pd.concat(chunks)

print(df.count())
print(df.size)
