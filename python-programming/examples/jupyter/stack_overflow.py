%config IPCompleter.greedy=True
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# The following might not work on your computer if it does not have enough free memory
df = pd.read_csv('survey_results_public.csv')
df

df.size # size in memory 7,555,055 it is too big if you only have 8gb memory

df.count()

df.info()

df.describe() # only few columns were identified to have numeric values

df.head(3)
