"""
Source : https://seaborn.pydata.org/introduction.html
"""

import seaborn as sns
import matplotlib

sns.set()
tips = sns.load_dataset("tips")
r = sns.relplot(
    x="total_bill",
    y="tip",
    col="time",
    hue="smoker",
    style="smoker",
    size="size",
    data=tips)
matplotlib.pyplot.show(r)
