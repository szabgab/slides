# Jupyter notebooks
{id: jupyter}


## Jupyter on Windows
{id: run-jupyter-windows}


On Windows install [Anaconda](https://www.anaconda.com/distribution/)
and then you'll be able to run Jupyter notebook from the start menu.


Alternatively:

```
pip install jupyter
```

## Jupyter on Linux and OSX
{id: run-jupyter-linux}

Install

For Linux and OSX I recommend using **virtualenv** and installing with **pip**.

```
virtualenv -p python3 ~/venv3
source ~/venv3/bin/activate
pip install jupyter
```

Run

```
cd examples/jupyter/
jupyter notebook
```

* Your browser should open. If not, there is a link in the terminal.


## Jupyter add
{id: jupyter-simple-add}


* Open an existing notebook (ipynb file). e.g examples/jupyter/add.ipynb
* Create new notebook.
* File - Save As
* ...
* Quit - shut down the notebook server.



```
def add(x, y):
    return x+y

add(2,3)
```


## Planets
{id: planets-csv}

![](examples/jupyter/planets.csv)


## Jupyter notebook Planets
{id: jupyter-notebook-planets}

![](examples/jupyter/planets.py)


## Jupyter StackOverflow
{id: jupyter-stackoverflow}

* Download the latest dataset from the [survey](https://insights.stackoverflow.com/survey).
* unzip the file. Feel free to remove the __MACOSX/ directory.

![](examples/jupyter/stack_overflow.py)


## Jupyter StackOverflow - selected columns
{id: jupyter-stackoverflow-load-selected-columns}


```
df = pd.read_csv('survey_results_public.csv', usecols=['Country', 'OpenSourcer', 'CompTotal'])
```


## Jupyter processing chunks
{id: jupyter-processing-chunks}

```
for chunk in pd.read_csv('survey_results_public.csv', chunksize=chunksize):
    process(chunk)
```


## Jupyter StackOverflow - selected rows
{id: jupyter-stackoverflow-load-selected-rows}

```
# Load only data from a specific country.

country_name = 'Israel'
df = None
for chunk in pd.read_csv('survey_results_public.csv', chunksize=10000):
    part = chunk[ chunk['Country'] == country_name ]
    if df is None:
        df = part.copy(deep = True)
    else:
        df = df.append(part.copy(deep = True), ignore_index = True)


df.count()
df.size
```



## Jupyter StackOverflow - biggest countries (in terms of number of responses)
{id: jupyter-stackoverflow-biggest-countries}

```
country_count = df['Country'].value_counts()
country_count

type(country_count) # pandas.core.series.Series
# country_count.__class__.__name__  # Series

# We can use it either as a dictionary or as a list
country_count['United States'] # 20949
# country_count[0] # 20949
# country_count['Israel']

# Take the top 20 countries
first20 = country_count.head(20)
first20
# type(first20) # Series

# first20 = country_count.iloc[0:20] # part of the Series
# first20
# type(first20) # Series

#first20 = country_count[0:20]
# first20
# type(first20) # Series

# Select rows of the "biggest" countries
first20.keys()
```



## Jupyter StackOverflow - historgram
{id: jupyter-stackoverflow-histogram}

```
# Historgram of the top 20 countries
first20.hist(bins = 20)

# Plot using Seaborn
plot = sns.relplot(data = first20)
plot.set_xticklabels(rotation=90)
```



## Jupyter StackOverflow - filter by country
{id: jupyter-stackoverflow-filter-by-country}

```
df['Country'] == 'Israel'
df [ df['Country'] == 'Israel' ]

df[ df['Country'].isin( ['India', 'Israel'] ) ]
df[ df['Country'].isin( first20.keys() ) ]
```


## Jupyter StackOverflow - OpenSourcer
{id: jupyter-stackoverflow-opensourcer}

```
df['OpenSourcer'].value_counts()

df['OpenSourcer'].unique()
```



## Jupyter StackOverflow - cross tabulation
{id: jupyter-stackoverflow-cross-tabulation}

```
# Crosstabulation
first10 = country_count.head(10)
subset = df[ df['Country'].isin( first10.keys() ) ]
# subset.count()

# subset['OpenSourcer'].value_counts()
grouped = subset.groupby('Country')['OpenSourcer'].value_counts()
# grouped.plot.bar(figsize=(15,15))

pd.crosstab(subset['Country'], df['OpenSourcer'])

ct = pd.crosstab(subset['Country'], df['OpenSourcer']).apply(lambda r: 100 * r/r.sum(), axis=1)
ct

ct.transpose().hist(figsize=(15, 15))
```



## Jupyter StackOverflow - salaries
{id: jupyter-stackoverflow-salaries}

```
# Try to show the average salary by country
grp = df.groupby('Country').mean().round({'CompTotal' : 0})
#grp['CompTotal']
pd.set_option('display.float_format', lambda x: '{:,}'.format(x))
grp.sort_values('CompTotal', ascending=False)
```



## Jupyter StackOverflow - replace values
{id: jupyter-stackoverflow-replace-values}

```
nd = df.replace({'OpenSourcer' : {
        'Never' : 0,
        'Less than once per year' : 1,
        'Less than once a month but more than once per year' : 2,
        'Once a month or more often' : 3,
       } })
nd
nd.describe()
nd.groupby('Country').mean().sort_values('OpenSourcer', ascending=False)
```


## Jupyter StackOverflow - selected rows
{id: jupyter-stackoverflow-more}

```
# Distribution of responses among countries.
# Relation of Open Source contribution to experience.
# Open Source contribution by country.
# Look at the pdf file and create similar reports for a specific country
```



## Jupyter notebook Intellisense (TAB completition)
{id: jupyter-notebook-intellisense}


```
%config IPCompleter.greedy=True
```


## Jupyter examples
{id: jupyter-examples}


```

examples/jupyter/planets.csv

examples/jupyter/planets.ipynb

examples/jupyter/numpy_matrix.ipynb

examples/jupyter/seaborn_tips.ipynb
```

## IPy Widgets
{id: ipywidgets}
{i: ipywidgets}

* [Interact](https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
* [Widget list](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html)

## Genes using Jupyter
{id: genes-using-jupyter}

```
cd examples/pandas/
jupyter notebook genes.ipynb
```


