# List assignment



List assignment works in "parallel" in Python.

{% embed include file="src/examples/lists/list_assignment.py" %}

```
x,y = f()  # works if f returns a list of 2 elements
```


It will throw a run-time ValueError exception if the number
of values in the returned list is not 2. (Both for fewer and for more return values).



