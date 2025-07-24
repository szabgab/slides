# Using modules exporting functions

```perl
use Cwd;
my $path = cwd;
```

Probably better this way,
so the reader will know where each function comes from
and we reduce the risk of redefining other functions by importing exactly the
functions we want.

```perl
use Cwd ('cwd');
my $path = cwd;
```

also written as

```perl
use Cwd qw(cwd);
my $path = cwd;
```

You can also make sure not to import anything and the use fully qualified names.


```perl
use Cwd ();
my $path = Cwd::cwd;
```









