#!/usr/bin/perl
use strict;
use warnings;

my @numbers = qw(8 2 5 3 1 7);
my @big_numbers = grep {$_ >= 5} @numbers;
print "@big_numbers\n";      # (8, 5, 7)
