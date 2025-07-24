# Integer division and the future


* __future__

{% embed include file="src/examples/numbers/divide.py" %}

```
$ python divide.py
1

$ python3 divide.py
1.5
```

{% embed include file="src/examples/numbers/future_divide.py" %}


If you need to use Python 2, remember that by default division is integer based so 3/2 would return 1.
Importing the 'division' directive from __future__ changes this to the behavior that we usually expect 3/2 being 1.5.
This is also the behavior we have in Python 3.
In case you already use Python 3 and would like to get the "old" behavior, that is to get the integer part of the division, you can
always call the "int" function: int(b/a).


