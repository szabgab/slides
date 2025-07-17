# Read CSV file as array of hashes

* csv

The csv function that can be imported from Text::CSV can read a CSV into memory, creating an array of hashes.

Element from the first row will be used as the keys of these hashes and elements from all the other rows will be used as
the values of these hashes.

* [Text::CSV](https://metacpan.org/pod/Text::CSV)

{% embed include file="src/examples/other/planets.csv" %}
{% embed include file="src/examples/other/read_csv_as_array_of_hashes.pl" %}
{% embed include file="src/examples/other/read_csv_as_array_of_hashes.out" %}


