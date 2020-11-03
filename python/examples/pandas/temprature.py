import sys
import pandas as pd

filename = 'temprature.csv'
df = pd.read_csv(filename)
print(df)
print()

def covid_instructions(row):
    return "stay home" if row['temp'] >= 38 else "go to work"

df['covid_instructions'] = df.apply(covid_instructions, axis=1)

print(df)
