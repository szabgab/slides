# Process slides
{id: process-slides}

## Page One
{id: page-one}


```
use strict;
use warnings;
```

## Page Two
{id: page-two}
{i: $SIG}
{i: __WARN__}

[signal 7](http://kernel.org/doc/man-pages/online/pages/man7/signal.7.html)

Alternatively you could also insert the following in your code:
`use diagnostics;`
to get the explanations for every warning.
See also `perldoc perldiag` for a detailed explanation of each warning and error.


```
$SIG{KILL} = sub { print "KILL received\n"; exit;};  # kill -9  cannot catch it
$SIG{INT}  = sub { print "INT received\n";};         # kill -2  or Ctrl-C
$SIG{TERM} = sub { print "TERM received\n"; exit;};  # kill -15
$SIG{TSTP} = sub { print "TSTP received\n";};        # kill -20 or Ctrl-Z
```


## Unordered list
{id: unordered-list}

* Entry One
* Entry Two
* Entry Three

paragraph with backslash-d: \d and double-backslash-x: \\x


```
literallayout with backslash-s: \s
```


[Perl Arrays](https://perlmaven.com/perl-arrays)




## Ordered list
{id: ordered-list}

1. Entry One
1. Entry Two
1. Entry Three



An ini file has sections starting by the name of the section in square brackets and within
each section there are key = value pairs with optional spaces around the "=" sign.
The keys can only contain letters, numbers, underscore or dash.
In addition there can be empty lines and lines starting with # which are comments.

