"""
Anscombe's quartet
==================

_thumb: .4, .4

Source: https://seaborn.pydata.org/examples/anscombes_quartet.html 
"""
import seaborn as sns
import matplotlib
sns.set(style="ticks")

# Load the example dataset for Anscombe's quartet
df = sns.load_dataset("anscombe")

# Show the results of a linear regression within each dataset
r = sns.lmplot(
    x="x",
    y="y",
    col="dataset",
    hue="dataset",
    data=df,
    col_wrap=2,
    ci=None,
    palette="muted",
    height=4,
    scatter_kws={"s": 50, "alpha": 1})

matplotlib.pyplot.show(r)

