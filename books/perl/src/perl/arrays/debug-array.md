# Debugging an array

* Data::Dumper
* Dumper
* \@

{% embed include file="src/examples/perlarrays/debug.pl" %}

```
Moose Barney Foo Bar
Moose Barney Foo Bar
$VAR1 = [
          'Moose',
          'Barney',
          'Foo',
          'Bar'
        ];
$VAR1 = [
          'Moose',
          'Barney',
          'Foo Bar'
        ];
```


