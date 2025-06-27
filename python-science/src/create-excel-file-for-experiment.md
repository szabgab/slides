# Create Excel file for experiment with random data


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
{% embed include file="src/examples/pandas/genome_create_excel.py" %}

**Output:**

{% embed include file="src/examples/pandas/genome_create_excel.out" %}


