import pandas as pd

filename = 'data.csv'
df = pd.read_csv(filename)

print(df)
print()


def combine_two_columns(row):
    return row['lname'] + '_' + row['fname']

df['combined'] = df.apply(combine_two_columns, axis=1)
print(df)
print()


def combine_more_columns(row):
    columns = ['lname', 'age', 'fname']
    return '_'.join(map(lambda name: str(row[name]), columns))

df['combined'] = df.apply(combine_more_columns, axis=1)
print(df)


