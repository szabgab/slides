# Exercise: create a function that generates numbers multipliers

Create a function that given a number returns a subroutine reference.
Calling that subroutine with an array reference will then multiply each
value by the originally given number.


```perl
my $duplicate = multiplier_generator(2);

my @numbers = (2, 4, 7);
$duplicate->(\@numbers);
print "@numbers\n";   # 4 8 14
```


