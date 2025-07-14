# Exercise: Add many arrays

Pick up the examples/references/add_arrays.pl script that
can add two arrays and change it to accept any number of
array references.

Extra exercise: add parameters that will control to stop
the addition at the shortest array or the longest array.

```
my @a = (2, 3);
my @b = (4, 5, 6);
add('shortest', \@a, \@b); # returns (6, 8)
add('longest', \@a, \@b);  # returns (6, 8, 6)
```


