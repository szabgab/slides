#!/usr/bin/env perl
use strict;
use warnings;

my @numbers = (2, 4, 7);
multiply_by_two(\@numbers);
print "@numbers\n";   # 4 8 14

sub multiply_by_two {
    my ($ref) = @_;
    foreach my $number (@$ref) {
        $number *= 2;
    }
}
