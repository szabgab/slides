#!/usr/bin/env perl
use strict;
use warnings;

my @first  = (2, 3);
my @second = (7, 8, 5);
add(@first, @second);

sub add {
    my ($first, $second) = @_;
    print "$first\n";
    print "$second\n";
}

# 2
# 3

