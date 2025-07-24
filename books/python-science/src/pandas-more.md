# Pandas more


```
df.iloc[:, 4:10].sum(axis=1)

# rearrange order of columns
cols = list(df.columns)
df = df[ cols[0:4], cols[-1], cols[4:20] ]

to_csv('file.csv', index=False)

read_csv(filename, delimiter='\t')
to_csv(filename, sep='\t')


# after filtering out some rows:
df = df.reset_index()
df.reset_index(drop=True, inplace=True)


filter with
df.loc[ ~df['Name'].str.contains('substring') ]

can also have regex=True parameter

# replace values
df[ df['Name'] == 'old', 'Name' ] = 'new'
```


