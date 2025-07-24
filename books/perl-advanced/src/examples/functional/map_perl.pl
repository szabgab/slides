#!/usr/bin/perl
use strict;
use warnings;

my @numbers = (1, 4, 7, 3);
my @doubles = map {$_ * 2} @numbers;
print "@doubles\n";  # 2 8 14 6
