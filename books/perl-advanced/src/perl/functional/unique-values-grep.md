# Unique values using grep



Of course there is an even shorter way to write it:

{% embed include file="src/examples/functional/unique_values_grep.pl" %}

In this version you can even assign the values back to the original
array writing:

```
@data = grep { !$seen{$_}++} @data;
```


