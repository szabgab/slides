import pandas as pd
import numpy as np
import datetime
import sys

if len(sys.argv) < 2:
    exit("Need filename")
filename = sys.argv[1]

def calculate_averages(df):
    v1 = df.iloc[:, 0:3].mean(axis=1)  # axis=1 -> calculate the mean row-wise
    v2 = df.iloc[:, 3:6].mean(axis=1)
    return np.log2(v1/v2)

start = datetime.datetime.now()
df = pd.read_excel(filename, index_col='genome name')
print(df.head())
print(datetime.datetime.now() - start)

calculated_value = calculate_averages(df)
print(datetime.datetime.now() - start)

threshold = 0.2
filtered_df = df[calculated_value > threshold]
print(filtered_df.head())
print(datetime.datetime.now() - start)
