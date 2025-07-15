# Array slices

{% embed include file="src/examples/advanced-perl/array_slices.pl" %}

A few more examples

```
my @i = (3, 5, 7);
print "@i\n";                           # 3 5 7
print "@letters[@i]\n";                 # d f h
print "@letters[split ' ', '3 5 7']\n"; # d f h
```


