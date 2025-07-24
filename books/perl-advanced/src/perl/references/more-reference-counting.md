# More Reference Counting


```
my @names     = qw(Foo Bar Baz);   # cnt = 1
my $names_ref = \@names;           # cnt = 2
my $other_ref = \@names;           # cnt = 3
my $x_ref     = $names_ref;        # cnt = 4

$other_ref = undef;            # cnt = 3
```


