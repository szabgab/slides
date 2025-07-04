# like(value, qr/expected regex/, name);


What if you don't want or can't realisticly expect an exact match with the result?

You can use `like` that compares with regex `=~`.

{% embed include file="src/examples/test-more/show_last_update.pl" %}

```
This page was last updated at 2020-11-10T09:19:38
```

{% embed include file="src/examples/test-more/t/last_update.t" %}

```
prove t/last_update.t
```

{% embed include file="src/examples/test-more/t/last_update.t.out" %}


