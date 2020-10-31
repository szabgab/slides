import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = './developer_survey_2020/survey_results_public.csv'

df = pd.read_csv(file, sep = ',')

totals = []
countries = []
for c in np.unique(list(df['Country'])):

    totals.append(len(df[df['Country'] == c]))
    countries.append(c)

plt.figure()
plt.bar(np.arange(0, len(countries)), totals)
plt.xticks(np.arange(0, len(countries)), countries)



#%%

age_totals = []
ages = []
for c in np.unique(list(df['Age1stCode'])):

    age_totals.append(len(df[df['Age1stCode'] == c]))
    ages.append(c)

plt.figure()
plt.scatter(ages, age_totals)
plt.xticks(fontsize = 5)




