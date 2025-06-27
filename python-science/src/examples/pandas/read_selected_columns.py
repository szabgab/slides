import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]


df = pd.read_csv(filename, usecols=['Country', 'OpenSourcer', 'CompTotal'])
print(df.head())

