"""
Source : https://seaborn.pydata.org/introduction.html
"""

import seaborn as sns

sns.set()
tips = sns.load_dataset("tips")  # Reads into Pandas DataFrame
#print(type(tips))

plot = sns.relplot(
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
    data=tips)
#print(type(plot))
plot.savefig("out.png")
#matplotlib.pyplot.show(r)
#matplotlib.pyplot.savefig(r)
