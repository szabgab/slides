# What is a CSV file?

* CSV stands for Comma Separated Values
* A CSV file is similar to the values you might put in an Excel file. Though in Excel each cell has both a `value` and a `format` (and maybe more) attributes. A CSV file only contains values.
* A CSV file has rows and in each row there are values separated by a comma.
* In some cases the separator is some other character. e.g. a semic-colon (`;`), a pipeline (`|`) or a TAB character. (The last one is also referred to a TSV file where TSV stands for TAB Separated Values.

* There are a number of other variations, so the csv-reading and writing librariers usually provide options to handle these variations.

* Sometimes all the lines hold values. Sometimes the first line acts as the list of column-names.

