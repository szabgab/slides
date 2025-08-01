# Multiprocess N files: Pool

* multiprocess
* Pool
* map


In this example we "analyze" files by counting how many characters they have, how many digits, and how many spaces.


Analyze N files in parallel.

{% embed include file="src/examples/multiprocess/multiprocess_files.py" %}

```
$ python multiprocess_files.py 3 multiprocess_*.py
```

{% embed include file="src/examples/multiprocess/multiprocess_files.out" %}


We asked it to use 3 processes, so looking at the process ID you can see one of them worked twice.
The returned results can be any Python datastructure. A dictionary is usually a good idea.


