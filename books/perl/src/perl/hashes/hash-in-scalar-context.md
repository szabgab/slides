# Hash in scalar context

A hash in LIST context returns its keys and values.

```perl
my @foobar = %user;
```

In SCALAR context:


```perl
if (%user) {
    # the hash is not empty
}
```



