# use, require and import

```perl
require Math::Calc;
```

```perl
use Math::Calc qw(add);
```

```perl
BEGIN {
    require Math::Calc;
    Math::Calc->import( qw(add) );
}
```

* `use` is executed at compile time, just as a `BEGIN` block.
* `require is executed at run time so if we don't enclose it in a `BEGIN` block it will happen later.

```perl
if ($holiday) {
    use Vaction::Mode;
}
```

The above does not make much sense as the `use` will load the module
at compile time regardless of day.



```perl
if ($holiday) {
    require Vacation::Mode;
    Vacation::Mode->import;
}
```


And we don't even need to call import() if we don't care about that.

