# shift

* shift

{% embed include file="src/examples/script/shift.sh" %}

```
$ ./examples/script/shift.sh foo bar moo qux zorg
foo bar moo qux zorg
bar moo qux zorg
qux zorg
```

shift can move the content of $* to the left by N elements (defaults to 1)
Mostly to avoid dealing with ${10}.



