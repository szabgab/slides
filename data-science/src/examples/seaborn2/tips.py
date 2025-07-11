"""
Source : https://seaborn.pydata.org/introduction.html
"""

import seaborn as sns

sns.set()  # Apply the default default seaborn theme, scaling, and color palette. Optional.

tips = sns.load_dataset("tips")  # Load example dataset into Pandas DataFrame
#print(type(tips))

# print(tips)

plot = sns.relplot(
    x = "total_bill",
    y = "tip",
    col = "time",
    hue = "smoker",
    style = "smoker",
    size = "size",
    data = tips)

# print(type(plot))    # seaborn.axisgrid.FacetGrid
plot.savefig("tips.png")
