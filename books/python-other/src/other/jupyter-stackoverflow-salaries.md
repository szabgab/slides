# Jupyter StackOverflow - salaries

```python
# Try to show the average salary by country
grp = df.groupby('Country').mean().round({'CompTotal' : 0})
#grp['CompTotal']
pd.set_option('display.float_format', lambda x: '{:,}'.format(x))
grp.sort_values('CompTotal', ascending=False)
```



