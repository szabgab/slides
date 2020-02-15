# Pandas
{id: pandas}

## Pandas
{id: about-pandas}

* [Pandas](https://pandas.pydata.org/) Python Data Analysis Library
* Handle data sequences
* [A Beginner's Guide to Optimizing Pandas Code for Speed](https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6)

## Planets
{id: planets}

![](examples/pandas/planets.csv)


## Pandas Planets - Dataframes
{id: pandas-read-csv-planets}

![](examples/pandas/read_csv_planets.py)

```
         distance        mass
name
Mercury      0.40    0.055000
Venus        0.70    0.815000
Earth        1.00    1.000000
Mars         1.50    0.107000
Ceres        2.77    0.000150
Jupiter      5.20  318.000000
Saturn       9.50   95.000000
Uranus      19.60   14.000000
Neptune     30.00   17.000000
Pluto       39.00    0.002180
Charon      39.00    0.000254
```


```
         distance     mass        dm
name
Mercury      0.40  0.05500  0.022000
Venus        0.70  0.81500  0.570500
Earth        1.00  1.00000  1.000000
Mars         1.50  0.10700  0.160500
Ceres        2.77  0.00015  0.000415
```


```
         distance   mass      dm
name
Jupiter       5.2  318.0  1653.6
Saturn        9.5   95.0   902.5
```


## Pandas Stocks
{id: pandas-stocks}
![](examples/pandas/stocks.py)


## Pandas Stocks
{id: pandas-read-csv-stocks}
![](examples/pandas/read_csv_stocks.py)


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




