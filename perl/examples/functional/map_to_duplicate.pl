#!/usr/bin/perl
use strict;
use warnings;

my @numbers = (1, 4, 17);
my @big_numbers = map {($_, $_)} @numbers;
print "@big_numbers\n";  # 1 1 4 4 17 17

