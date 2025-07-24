# Test::More is(  value,   expected_value,   name);

* is


It would be much better to see the expected value and the actually received value.
This usually helps in locating the problem.


{% embed include file="src/examples/test-more/t/32.t" %}

```
perl t/32.t
```

{% embed include file="src/examples/test-more/t/32.t.out" %}

See, in this case we can already guess that it cannot add 3 values.

* `is` compares using `eq`



