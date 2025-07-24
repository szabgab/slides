# Logging Exceptions

* __DIE__

```
$SIG{__DIE__} = sub { logger('error', $_[0]) };
```
{% embed include file="src/examples/advanced-perl/die_handler.pl" %}


