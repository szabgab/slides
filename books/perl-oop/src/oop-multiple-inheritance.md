# Multiple inheritance


* multiple inheritance

```
use parent 'A', 'B';
use parent qw(A B);

use base 'A', 'B';
use base qw(A B);

our @ISA = ('A', 'B');
our @ISA = qw(A B);
```



