import sys
import pandas as pd

filename = "survey_results_public.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]
country_name = 'Israel'
chunks = []
dev_chunks=[]
for chunk in pd.read_csv(filename, usecols=['Country','DevType'],chunksize=10000):
    part = chunk[chunk['Country'] == country_name]


    print(chunk.size)
    print(part.size)
    print('--')
    chunks.append(part)


df = pd.concat(chunks)
print(df.dtypes)
for value in ['Academic researcher','Data or business analyst', 'Data scientist or machine learning specialist','Database administrator','Designer', 'Developer, back-end',
              'Developer, desktop or enterprise applications','Developer, embedded applications or devices','Developer, front-end','Developer, full-stack','Developer, game or graphics', 'Developer, mobile','Developer, QA or test',
              'DevOps specialist','Educator','Engineer, data', 'Engineer, site reliability','Engineering manager', 'Marketing or sales professional', 'Product manager', 'Scientist',
              'Senior Executive (C-Suite, VP, etc.)', 'System administrator']:
    print(value)
    df[value]= df.apply(lambda row: value in row['DevType'], axis=1)

print(df.count())
print(df.size)


