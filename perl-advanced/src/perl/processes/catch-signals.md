# Catch signals

{% embed include file="src/examples/signals/catch_signals.pl" %}

```
$SIG{$name} = sub {};     # do something when signal received
$SIG{$name} = 'IGNORE';   # ignore it
$SIG{$name} = 'DEFAULT';  # reset to the default behavior
```


 - [Catch Ctrl-C](./perl/processes/catch-ctrl-c.md)

{% embed include file="src/examples/signals/catch_ctr_c.pl" %}


