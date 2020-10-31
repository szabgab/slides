import pandas

df=pandas.read_csv("survey_results_public.csv")

countrey_dist=df['Country'].value_counts()

open_sourcers_dist=df['OpenSourcer'].value_counts()

print("top 10 response countries:\n",countrey_dist.head(10))

open_sourcers_dist_top=df['OpenSourcer'][df['Country']=='United States'].value_counts()
experience_dist_top=df['YearsCode'][df['Country']=='United States'].value_counts()

print('distribution of open sourcer is the top country USA is :\n' ,open_sourcers_dist_top)
print('distribution of  experience in the top country USA is:\n' ,experience_dist_top)


df=df[['OpenSourcer','YearsCode']][df['Country']=='United States']
df_agg=df.groupby('OpenSourcer').agg('YearsCode')

print("relationship betwen OpenSourcer to coding exprience in US is :\n",df_agg)

