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

## Pandas Read CSV various datatypes
{id: pandas-read-csv-various-datatypes}

{aside}
Example with a few more column-types (e.g. the column with the title MyBool contains True and False values and it is recognized as bool)
{/aside}

![](examples/pandas/mixed.csv)

![](examples/pandas/mixed.py)

![](examples/pandas/mixed.out)

## Pandas Read CSV set dtype
{id: pandas-read-csv-set-dtype}

{aside}
When recognizing integers read_csv will default to int64, but if we would like to save memory we can set the dtype while we read the file.
{/aside}

![](examples/pandas/mixed_set_dtype.py)

![](examples/pandas/mixed_set_dtype.out)


## Pandas Read CSV convert values
{id: pandas-read-csv-convert-values}

{aside}
Sometime the data in the CSV file represents something else or we might want to change the meaning of the data.

For example in some  cases 0 represents False and 1 represents True. If the CSV file contains 0 and 1 values in a column Pandas will automatically represent them as integers.
We can convert them to False and True values respectively.

In another case we might have exit-codes in a column where 0 means success and any other number means failure. We might want to simplify that column and represent success by True
and failure by False. (Yes, we loose the details of the failure, but maybe we are not interested in the details.)

This latter is what we can see in our example.
{/aside}

![](examples/pandas/mixed_convert_values.py)

![](examples/pandas/mixed_convert_values.out)


## Pandas split multivalue column into separate columns
{id: pandas-split-multivalue-column}

![](examples/pandas/multivalue.csv)

![](examples/pandas/multivalue.py)

![](examples/pandas/multivalue.out)

## Pandas split multivalue column into separate columns - get_dummies
{id: pandas-split-multivalue-column}
{i: get_dummies}

![](examples/pandas/multivalue_get_dummies.py)

![](examples/pandas/multivalue_get_dummies.out)


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

## DataFrame filter rows by value
{id: pandas-planets-filter-rows-by-value}

![](examples/pandas/planets_filter_row_by_value.py)
![](examples/pandas/planets_filter_row_by_value.out)


## DataFrame filter rows by value in list
{id: pandas-planets-filter-rows-by-value-in-list}

![](examples/pandas/planets_filter_row_by_value_in_list.py)
![](examples/pandas/planets_filter_row_by_value_in_list.out)

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

## Count values
{id: count-values}

![](examples/pandas/so_value_counts.py)

## Select top items
{id: select-top-items}

* StackOverflow - biggest countries (in terms of number of responses)

![](examples/pandas/so_top_countries.py)

## Pandas Show histogram
{id: pandas-show-histogram}

![](examples/pandas/so_histogram.py)
![](examples/pandas/so_histogram.png)

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
* Distribution of responses among countries.
* Relation of Open Source contribution to experience.
* Open Source contribution by country.
* Look at the pdf file and create similar reports for a specific country

* Pick a dataset from [Kaggle](https://www.kaggle.com/datasets) and try to analyze that.



