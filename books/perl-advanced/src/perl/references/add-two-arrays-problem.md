# Add two (or more) arrays

* @_

```
Let's extend it so it will be able to take two vectors (arrays) and add
them pair-wise.  (2, 3) + (7, 8, 5) =  (9, 11, 5)
```

{% embed include file="src/examples/references/fail_to_add_arrays.pl" %}


The problem is, @_ in the add function will get (2, 3, 7, 8, 5);
We cannot know where does the first array end and where the second begins.

(I am sure one can come up with a complex way of prefixing the real data
by meta information that describes the data, but why work so hard if Perl
already has the tools you need?)



