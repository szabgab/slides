# Using Context Manager

```
with cm_for_sample():
    start
    do
    do
    if we are done early:
        return early-end
    do
    bad-code    (raises exception)
    do
```

* `cleanup` happens automatically, it is defined inside the `cm_for_sample`


