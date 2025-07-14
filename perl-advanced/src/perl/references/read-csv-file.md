# Read CSV file

* CSV

{% embed include file="src/examples/references/data.csv)

```
We would like to read in that file and be able to access the fname of row 5
as  $data[3]{fname}

# the fname on line 5 is in index 3 because: 
# line 1 is the header
# line 2 is element 0 in the array
# ...
# line 5 is element 3 in the array
```
{% embed include file="src/examples/references/read_csv_file.pl" %}
{% embed include file="src/examples/references/read_csv_file.out" %}


