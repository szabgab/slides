import pandas as pd
import numpy as np
import datetime
import sys

filename = 'raw_data.xlsx'
if len(sys.argv) == 2:
    filename = sys.argv[1]

def calculate_averages(row):
    v1 = row.iloc[0:3].mean()
    v2 = row.iloc[3:6].mean()
    return np.log2(v1/v2)

start_time = datetime.datetime.now()
df = pd.read_excel(filename, index_col='genome name')
load_time = datetime.datetime.now()
print(load_time - start_time)

print(df.head())

calculated_value = df.apply(calculate_averages, axis=1)

threshold = 0.2
filtered_df = df[calculated_value > threshold]

print(filtered_df.head())

calculate_time = datetime.datetime.now()
print(calculate_time - load_time)


