# Use flag to skip first few lines

We have a series of rows that we might read from a file and would like to process the sections of rows that start with a well-defined row. Unfortunately the file does not always start with a row that matches the definition. In some cases there are a few lines at the beginning of the file that we need to throw away before we can start our processing.

In this exacmple we use series of numbers to represent the rows of that file and the "well defined condtion to start the series is a number being "big".

We can use a variable as a "flag" to indicate if we are still before the first good section or if the sections already started.

{% embed include file="src/examples/boolean/print_series_staring_with_big_number.py" %}

