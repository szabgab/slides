# Debugging Queue



The following implementation has a bug. (Even though the n was supposed to remove the element
and the code seems to mean that it does, we still see two items after we removed the first.)

The question is how to debug this?



{% embed include file="src/examples/lists/queue_with_bug.py" %}

```
your name: Foo
your name: Bar
your name: n
Foo
your name: s
2
```


