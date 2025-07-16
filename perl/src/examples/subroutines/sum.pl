#!/usr/bin/perl
use strict;
use warnings;

print sum(3, 7, 11, 21), "\n";
print sum(1, 2, 3), "\n";

sub sum {
    my $sum = 0;
    foreach my $v (@_) {
        $sum += $v;
    }
    return $sum;
}

