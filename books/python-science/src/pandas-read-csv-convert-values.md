# Pandas Read CSV convert values



Sometime the data in the CSV file represents something else or we might want to change the meaning of the data.

For example in some  cases 0 represents False and 1 represents True. If the CSV file contains 0 and 1 values in a column Pandas will automatically represent them as integers.
We can convert them to False and True values respectively.

In another case we might have exit-codes in a column where 0 means success and any other number means failure. We might want to simplify that column and represent success by True
and failure by False. (Yes, we loose the details of the failure, but maybe we are not interested in the details.)

This latter is what we can see in our example.


{% embed include file="src/examples/pandas/mixed_convert_values.py" %}

{% embed include file="src/examples/pandas/mixed_convert_values.out" %}


