# String to float conversion

* parseFloat

use parseFloat


```
> c = "1.2"
> a+c
'231.2'
> a+parseInt(c)
24
> a+parseFloat(c)
24.2
```


Number(v) is like parseFloat.
Except that Number('4x') returns NaN
and parseInt('4x') and parseFloat('4x') both return 4.


