# Importing


```perl
use Module;
```

Every function (and variable) listed in the @EXPORT array is imported
automatically.

```perl
use Module ();
```

Nothing is imported.

```perl
use Module qw(foo bar);
```

Functions foo() and bar() are imported, nothing else.
Any function from the @EXPORT and @EXPORT_OK arrays can be requested to be imported.
There is also an %EXPORT_TAGS that can be used to define groups of functions to be imported.


