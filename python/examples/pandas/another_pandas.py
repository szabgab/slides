import pandas as pd
import matplotlib.pyplot as plt

filepath=r'survey_results_public.csv'

df=pd.read_csv(filepath)
print("The dataframe columns are:\n",list(df.columns))
print('-'*30)
#Let's check what kind of dtypes is in each column,
#if stats can be extracted - print it
for i in range(len(df.dtypes.index)):
    print(df.dtypes.index[i] , 'is of type ', df.dtypes[i])
    if df.dtypes[i]=='float64':
        print('*'*10,"\nAnd it's statistics:")
        print(df[df.dtypes.index[i]].describe())

#who is the most responsive country?
most_responsive_country=df['Country'].value_counts().index[0]
#now let's check what is the average working time per week for the most responsive country
most_responsive_country_df=df[df['Country']==most_responsive_country]
average_working_time_weekly=most_responsive_country_df['WorkWeekHrs'].mean()

#back to the original df, see what is the study fields distribution
#and then plotting it as a bar chart
study_fields_normalized=df['UndergradMajor'].value_counts(normalize=True)
fig,ax=plt.subplots()
ax.barh(list(study_fields_normalized.index),list(study_fields_normalized*100))
ax.set_xlabel("Relative Distribution")
fig.show()
