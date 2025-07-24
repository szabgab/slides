# Test::More isnt( value, not_expected_value,  name);

* isnt

Sometimes you are expecting to get a value but you don't really know what.
You just know one specific value that you want to make sure you have not
received.

{% embed include file="src/examples/test-perl/t/isnt.t" %}

```
perl t/isnt.t
```

{% embed include file="src/examples/test-perl/t/isnt.t.out" %}

This isn't a good example though.

