#!/usr/bin/perl
use strict;
use warnings;

my $sum = add(2, 3);
print "$sum\n";
print add(5, 8), "\n";

my $result = add2(4, 7);
print "$result\n";

sub add {
    my ($x, $y) = @_;

    my $z = $x+$y;
    return $z;
}

sub add2 {
    my $x = shift;
    my $y = shift;

    return $x+$y;
}

sub add_ugly {
    return $_[0]+$_[1];
}


