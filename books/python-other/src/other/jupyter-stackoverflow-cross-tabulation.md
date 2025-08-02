# Jupyter StackOverflow - cross tabulation

```python
# Crosstabulation
first10 = country_count.head(10)
subset = df[ df['Country'].isin( first10.keys() ) ]
# subset.count()

# subset['OpenSourcer'].value_counts()
grouped = subset.groupby('Country')['OpenSourcer'].value_counts()
# grouped.plot.bar(figsize=(15,15))

pd.crosstab(subset['Country'], df['OpenSourcer'])

ct = pd.crosstab(subset['Country'], df['OpenSourcer']).apply(lambda r: 100 * r/r.sum(), axis=1)
ct

ct.transpose().hist(figsize=(15, 15))
```





