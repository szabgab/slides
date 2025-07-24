import pandas as pd
import numpy as np
import datetime
import sys

if len(sys.argv) < 2:
    exit("Need filename")
filename = sys.argv[1]

def calculate_averages(df_numpy):
    v1 = df_numpy[:, 0:3].mean(axis=1)
    v2 = df_numpy[:, 3:6].mean(axis=1)
    return np.log2(v1/v2)

start = datetime.datetime.now()
df = pd.read_excel(filename, index_col='genome name')
print(df.head())
print(datetime.datetime.now() - start)

# the .values attribute changes from Pandas to numpy array
# (no more iloc, no headers, no index)
calculated_value = calculate_averages(df.values)
print(datetime.datetime.now() - start)

threshold = 0.2
filtered_df = df[calculated_value > threshold]
print(filtered_df.head())
print(datetime.datetime.now() - start)
