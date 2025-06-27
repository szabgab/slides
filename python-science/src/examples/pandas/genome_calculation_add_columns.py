import pandas as pd
import numpy as np
import datetime
import sys

if len(sys.argv) < 2:
    exit("Need filename")
filename = sys.argv[1]


def calculate_averages(row):
    v1 = row.iloc[0:3].mean()
    v2 = row.iloc[3:6].mean()
    return np.log2(v1/v2)

start = datetime.datetime.now()
df = pd.read_excel(filename, index_col='genome name')
print(df.head())
print(datetime.datetime.now() - start)

# create a new column of the calculated value
df['calculated_value'] = df.apply(calculate_averages, axis=1)
print(datetime.datetime.now() - start)

threshold = 0.2
filtered_df = df[df['calculated_value'] > threshold]
print(filtered_df.head())
print(datetime.datetime.now() - start)
