#!/usr/bin/perl
use strict;
use warnings;

my @numbers = (1..5);
my @doubles = map {$_ * 2} @numbers;
print "@doubles\n";    # 2 4 6 8 10


my @riches = map { $_ > 3 ? ($_+1, $_+2) : () } @numbers;
print "@riches\n"; # 5 6 6 7
