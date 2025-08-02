# Jupyter StackOverflow - replace values

```python
nd = df.replace({'OpenSourcer' : {
        'Never' : 0,
        'Less than once per year' : 1,
        'Less than once a month but more than once per year' : 2,
        'Once a month or more often' : 3,
       } })
nd
nd.describe()
nd.groupby('Country').mean().sort_values('OpenSourcer', ascending=False)
```




