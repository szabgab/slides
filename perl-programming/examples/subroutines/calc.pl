#!/usr/bin/perl
use strict;
use warnings;

my ($sum, $multi) = calc(3, 4);
print "Sum:   $sum\n";    # 7
print "Multi: $multi\n";  # 12

sub calc {
    my ($x, $y) = @_;

    return $x + $y, $x * $y;
}

