# Exercise: File reader with records

In a file we have "records" of data. Each record starts with three bytes in which we have the length of the record.
Then the content.

```
8 ABCDEFGH 5 XYZQR
```

Given this source file

{% embed include file="src/examples/generators/rows.txt" %}

using this code

{% embed include file="src/examples/generators/rows_to_records.py" %}

we can create this file:

{% embed include file="src/examples/generators/records.txt" %}

The exercise is to create an iterator/generator that can read such a file record-by-record.


