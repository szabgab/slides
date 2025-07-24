# Implicit stricture

* v5.12

no need to write use strict any more

```perl
use v5.12;
$x = 23;
say $x;
```

```
Global symbol "$x" requires explicit package name at a.pl line 3.
Global symbol "$x" requires explicit package name at a.pl line 4.
Execution of a.pl aborted due to compilation errors.
```


