# Use recent version of Perl

Before we go on learning about Object Oriented programming in Perl, let's mention a small improvement you can get when using a relatively recent version of perl.

Starting from version 5.36 that was released on 2022-05-28 we can write

```perl
use v5.36;
```

or

```perl
use 5.036;
```

and that will already turn on both `strict` mode and `warnings` and it will also include all the features that came with that version, including the `say` function.

So if we can require that our code will run on a perl version 5.36 or later then we can replace these 3 rows:

```perl
use strict;
use warnings;
use feature 'say';
```

with a single `use`-statement.
