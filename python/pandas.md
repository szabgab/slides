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

* Download one of the datasets from the [Stack Overflow survey](https://insights.stackoverflow.com/survey)
* unzip the file. Feel free to remove the `__MACOSX/` directory if it is still there.

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

## DataFrame filter columns by name
{id: pandas-planets-filter-columns-by-name}

![](examples/pandas/planets_filter_cols_by_name.py)
![](examples/pandas/planets_filter_cols_by_name.out)

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


## Pandas Planets - Add calculated column, remove / delete column (drop)
{id: pandas-add-column}

![](examples/pandas/add_column_drop_column.py)
![](examples/pandas/add_column_drop_column.out)

## Pandas Planets - calculate
{id: pandas-plantes-calculate}

![](examples/pandas/planets_calculate.py)
![](examples/pandas/planets_calculate.out)

## Pandas read CSV set index column
{id: pandas-read-csv-set-index-column}

![](examples/pandas/read_csv_set_index.py)
![](examples/pandas/read_csv_set_index.out)


## Pandas read selected columns
{id: pandas-read-selected-columns}

![](examples/pandas/read_selected_columns.py)

## Pandas read file in chunks
{id: pandas-read-file-in-chunks}

![](examples/pandas/read_file_in_chunks.py)

## Pandas read selected rows in chunks
{id: pandas-read-in-chunks-select-rows}

![](examples/pandas/read_file_in_chunks_select_rows.py)

![](examples/pandas/read_file_in_chunks_select_rows_append.py)

## Combine columns to create a new column
{id: pandas-combine-columns}
{i: apply}

![](examples/pandas/data.csv)
![](examples/pandas/create_column.py)
![](examples/pandas/create_column.out)

## Pandas read Excel
{id: pandas-read-excel}
{i: read_excel}

![](examples/pandas/read_excel.py)

## Create Excel file for experiment with random data
{id: create-excel-file-for-experiment}

Input is an Excel file with the following columns:

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
![](examples/pandas/genome_create_excel.out)


## Calculate Genome metrics
{id: calculate-genome-metrics}

![](examples/pandas/genome_calculation.py)

## Exercise: Pandas
{id: exercise-pandas}

* Take the Stack Overflow survey and the report created by SO.
* Repeate some of the calculations, but using only the data from a specific country

* Pick a dataset from [Kaggle](https://www.kaggle.com/datasets) and try to analyze that.

