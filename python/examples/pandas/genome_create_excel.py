import numpy as np
import pandas as pd
import datetime
import sys

if len(sys.argv) < 2:
    exit("Need number of rows")

rows_num = int(sys.argv[1])
cols_num = 6

start = datetime.datetime.now()
x = np.random.rand(rows_num, cols_num)

genome_names = list(map(lambda i: f'g{i}', range(rows_num)))
column_names = list(map(lambda i: f'm{i}', range(cols_num)))

df = pd.DataFrame(x, index=genome_names, columns=column_names)
df.index.name = 'genome name'

print(df.head())
print(datetime.datetime.now() - start)
df.to_excel('raw_data.xlsx')
print(datetime.datetime.now() - start)
