# Pandas
{id: pandas}

## Pandas
{id: about-pandas}

* [Pandas](https://pandas.pydata.org/) Python Data Analysis Library
* Handle data sequences
* [A Beginner's Guide to Optimizing Pandas Code for Speed](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)

## Datasets
{id: datasets}

* Planets
* StackOverflow survey

## Planets data
{id: planets-data}

![](examples/pandas/planets.csv)

## StackOverflow Survey data
{id: stackoverflow-survey-data}

* Download one of the dataset from the [survey](https://insights.stackoverflow.com/survey)
* unzip the file. Feel free to remove the `__MACOSX/` directory if it is there.

## Planets - Read CSV into Dataframes
{id: pandas-planets-read-csv}
{i: read_csv}

![](examples/pandas/read_csv.py)

![](examples/pandas/read_csv.out)

## Planets - DataFrame Statistics
{id: pandas-planets-statistics}
{i: columns}
{i: dtypes}
{i: index}
{i: values}
{i: describe}

![](examples/pandas/dataframe_stats.py)

![](examples/pandas/dataframe_stats.out)

## Planets - Show first and last rows
{id: pandas-planets-show-first-and-last-rows}
{i: head}
{i: tail}

* `head` will show the first few rows (defaults to 5)
* `tail` will show the last few rows (defaults to 5)

![](examples/pandas/planets_head_tail.py)

![](examples/pandas/planets_head_tail.out)

## Planets DataFrame select columns
{id: pandas-planets-select-columns}

![](examples/pandas/planets_select_columns.py)
![](examples/pandas/planets_select_columns.out)


## Planets DataFrame select rows
{id: pandas-planets-select-rows}

![](examples/pandas/planets_select_rows.py)
![](examples/pandas/planets_select_rows.out)

## Planets DataFrame select rows and columns
{id: pandas-planets-select-rows-and-columns}

![](examples/pandas/planets_rows_columns.py)
![](examples/pandas/planets_rows_columns.out)

## DataFrame filter rows by size
{id: pandas-planets-filter-rows-by-size}

![](examples/pandas/planets_filter_rows_by_size.py)
![](examples/pandas/planets_filter_rows_by_size.out)

## DataFrame filter rows by name
{id: pandas-planets-filter-rows-by-name}

![](examples/pandas/planets_filter_rows_by_name.py)
![](examples/pandas/planets_filter_rows_by_name.out)

## DataFrame filter elementwise boolean and
{id: pandas-planets-filter-elementwise-boolean-and}

![](examples/pandas/planets_filter_elementwise.py)
![](examples/pandas/planets_filter_elementwise.out)

## DataFrame sort (sort_values)
{id: pandas-planets-sort}
{i: sort_values}

![](examples/pandas/planets_sort.py)
![](examples/pandas/planets_sort.out)

## DataFrame loc vs. iloc
{id: pandas-planets-loc-vs-iloc}

* `loc` by values (here we start from the row where the index column == 3
* `iloc` by index (here we start from the 3rd row)

![](examples/pandas/planets_loc_vs_iloc.py)

![](examples/pandas/planets_loc_vs_iloc.out)


## Pandas Planets - Dataframes OLD
{id: pandas-read-csv-planets}

![](examples/pandas/read_csv_planets.py)

## Pandas Planets - calculate
{id: pandas-plantes-calculate}

![](examples/pandas/planets_calculate.py)
![](examples/pandas/planets_calculate.out)


## Merge Dataframes
{id: merge-dataframes}
![](examples/pandas/merge_dataframes.py)


## Analyze Alerts
{id: analyze-alerts}
![](examples/pandas/alerts.py)


## Analyze IFMetrics
{id: analyze-ifmetrics}
![](examples/pandas/ifmetrics.py)



## Create Excel file for experiment with random data
{id: create-excel-file-for-experiment}


Input is an excel file with the following columns:



```
genome name, c1, c2, c3, c4, c5, c6
```

* c1-c3 are numbers of cond1
* c4-c6 are numbers of cond2




We would like to filter to the lines that fulfill the following equations:



```
log2(avg(1-3) / avg(4-6)) > limit
other_limit > p.value( )
```
![](examples/pandas/genome_create_excel.py)


## Calculate Genome metrics
{id: calculate-genome-metrics}
![](examples/pandas/genome_calculation.py)


## Calculate Genome metrics - add columns
{id: calculate-genome-metrics-add-columns}
![](examples/pandas/genome_calculation_add_columns.py)


## Calculate Genome metrics - vectorized
{id: calculate-genome-metrics-vecorized}
![](examples/pandas/genome_calculation_vectorized.py)


## Calculate Genome metrics - vectorized numpy
{id: calculate-genome-metrics-vecorized-numpy}
![](examples/pandas/genome_calculation_vectorized_numpy.py)


## Genes using Jupyter
{id: genes-using-jupyter}

```
cd examples/pandas/
jupyter notebook genes.ipynb
```

## Combine columns
{id: pandas-combine-columns}

![](examples/pandas/data.csv)
![](examples/pandas/create_column.py)
![](examples/pandas/create_column.out)


## Pandas more
{id: pandas-more}

```
df.iloc[:, 4:10].sum(axis=1)

# rearrange order of columns
cols = list(df.columns)
df = df[ cols[0:4], cols[-1], cols[4:20] ]

to_csv('file.csv', index=False)
to_excel()

read_csv(filename, delimiter='\t')
to_csv(filename, sep='\t')


# after filtering out some rows:
df = df.reset_index()
df.reset_index(drop=True, inplace=True)


fileter with
df.loc[ ~df['Name'].str.contains('substring') ]

can also have regex=True parameter

# replace values
df[ df['Name'] == 'old', 'Name' ] = 'new'
```


## Pandas Series
{id: pandas-series}
{i: Series}
{i: values}
{i: index}
{i: RangeIndex}

![](examples/pandas/series.py)


## Pandas Series with names
{id: pandas-series-with-names}

![](examples/pandas/series_with_names.py)

* read excel
