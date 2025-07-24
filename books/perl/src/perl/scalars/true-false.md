# Boolean values: TRUE and FALSE

* undef
* defined
* boolean values
* TRUE
* FALSE

```perl
if ($z) {
    # $z is true
}
```

```perl
The FALSE values:

undef
""
0  0.0  00000  0e+10
"0"

All other values, such as the following are TRUE:

1
"00"
"0\n"
```


In many cases the separation must be between "real" values and undefined values.
For that you can use the `defined` function:



```perl
if (defined $x) {
    # $x is defined (not undef)
}
```


