# List Assignment

```
my ($x, $y, $z);

my ($x, $y, $z) = (1, "apple pie", 3.14);

($x, $y, $z) = f();   # where f() returns (2, 3, 7);
                      # nearly the same as $x=2; $y=3; $z=7;
($x, $y, $z) = f();   # where f() returns (8, 1, 5, 9);
                      # ignore 9
($x, $y, $z) = f();   # where f() returns (3, 4);
                      # $z will be undef
```

```
A regular question on job interviews:
How can we swap the values of 2 variables, let say $x and $y?
```


