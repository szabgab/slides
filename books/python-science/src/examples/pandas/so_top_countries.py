import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]

df = pd.read_csv(filename)

country_count = df['Country'].value_counts()

N = 20
# Take the top N countries
first = country_count.head(N)
print(first)
print(type(first)) # Series

# first = country_count.iloc[0:N] # part of the Series
# print(first)
# type(first) # Series

# first = country_count[0:N]
# print(first)
# type(first) # Series

# Select rows of the "biggest" countries
print(first.keys())

