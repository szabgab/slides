# note( message ) or diag( message );

* diag
* note

* `diag` prints out a message along with the rest of the output.
* `note()` does the same, but when running under the prove it does not show up.

Use it for whatever extra output in order to ensure that
your printouts will not interfere with future changes in the
test environment modules (such as `prove` or `Test::Harness`).


{% embed include file="src/examples/test-more/t/messages.t" %}

```
$ perl t/messages.t
```

{% embed include file="src/examples/test-more/t/messages.t.out" %}

```
prove t/messages.t
```

{% embed include file="src/examples/test-more/t/messages.t.prove.out" %}

```
prove -v t/messages.t
```

{% embed include file="src/examples/test-more/t/messages.t.prove-v.out" %}



