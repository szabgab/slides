# Exercise: Context manager

Create a few CSV file likes these:


{% embed include file="src/examples/context/a.csv" %}
{% embed include file="src/examples/context/b.csv" %}
{% embed include file="src/examples/context/c.csv" %}


Merge them horizontally to get this:


{% embed include file="src/examples/context/out.csv" %}

* Do it without your own context manager
* Create a context manager called myopen that accepts N filenames. It opens the first one to write and the other N-1 to read


```
with myopen(outfile, infile1, infile2, infile3) as out, ins:
    ...
```


