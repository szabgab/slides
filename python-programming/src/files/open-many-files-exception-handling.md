# Open many files - exception handling


{% embed include file="src/examples/files/average_from_files.py" %}
{% embed include file="src/examples/files/number_per_line.txt" %}
{% embed include file="src/examples/files/empty.txt" %}
{% embed include file="src/examples/files/number_per_line2.txt" %}

```
$ python average_from_files.py number_per_line.txt empty.txt number_per_line2.txt

Average:  58.25
trouble with 'empty.txt': Error: division by zero
Average:  3.5
```

```
$ python average_from_files.py numbers.txt

trouble with 'numbers.txt': Error: could not convert string to float: '23 345 12345\n'
```

```
$ python average_from_files.py more_numbers.txt

trouble with 'more_numbers.txt': Error: [Errno 2] No such file or directory: 'more_numbers.txt'
```


