#!/usr/bin/perl
use strict;
use warnings;

my @numbers = (1, 4, 17, 3, 28, 4);
my @big_numbers = map {$_ >= 10 ? $_ : ()} @numbers;
print "@big_numbers\n";  # 17 28
