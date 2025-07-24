# (note or diag) explain( a_variable );


* explain

* `explain();` will recognize if its parameter is a simple scalar or a reference to a more complex data structure.

Its result must be passed to either note(); does or diag();


{% embed include file="src/examples/test-more/t/explain.t" %}

```
perl t/explain.t
```

{% embed include file="src/examples/test-more/t/explain.t.out" %}



