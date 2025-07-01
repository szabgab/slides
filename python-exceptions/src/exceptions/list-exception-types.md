# List exception types

We can list more than one exceptions to be caught one after the other in a single "except" statement.


```
except (ZeroDivisionError, FileNotFoundError):
```
{% embed include file="src/examples/exceptions/handle_list_of_exceptions.py" %}

```
python handle_list_of_exceptions.py one.txt zero.txt two.txt three.txt
```



