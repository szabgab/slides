import numpy as np
import pandas as pd
import datetime
import sys

if len(sys.argv) < 2:
    exit("Need number of rows")

rows_num = int(sys.argv[1])
cols_num = 6

start_time = datetime.datetime.now()
matrix = np.random.rand(rows_num, cols_num)
#print(matrix)

genome_names = list(map(lambda i: f'g{i}', range(rows_num)))
column_names = list(map(lambda i: f'm{i}', range(cols_num)))

df = pd.DataFrame(matrix, index=genome_names, columns=column_names)
df.index.name = 'genome name'

print(df.head())


end_generate_time = datetime.datetime.now()
print(end_generate_time - start_time)

df.to_excel('raw_data.xlsx')

end_save_time = datetime.datetime.now()
print(end_save_time - end_generate_time)
