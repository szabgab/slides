import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

size = 10000

for df_chunk in pd.read_csv(filename, chunksize=size):
    print(df_chunk.head())
