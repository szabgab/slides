# Jupyter StackOverflow - historgram

```python
# Historgram of the top 20 countries
first20.hist(bins = 20)

# Plot using Seaborn
plot = sns.relplot(data = first20)
plot.set_xticklabels(rotation=90)
```


