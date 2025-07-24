import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

country_count = df['Country'].value_counts()
print(country_count)
print(type(country_count)) # pandas.core.series.Series

# We can use it either as a dictionary or as a list
print(country_count['United States']) # 12469
print(country_count[0]) # 12469
