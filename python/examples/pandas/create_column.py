import pandas as pd

filename = 'data.csv'
df = pd.read_csv(filename)
print(df)


def combine(row):
    return row['lname'] + '_' + row['fname']


df['combined'] = df.apply(combine, axis=1)
print(df)


def new_column(row):
    columns = ['lname', 'age', 'fname']
    return '_'.join(map(lambda name: str(row[name]), columns))

df['combined'] = df.apply(new_column, axis=1)
print(df)


