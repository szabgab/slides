#!/usr/bin/perl
use strict;
use warnings;


sub add {
    my ($x, $y) = @_;
    return $x+$y;
}

sub multiply {
    my ($x, $y) = @_;
    return $x*$y;
}

my %dispatch = (
    '+'  => \&add,
    '*'  => \&multiply,
);

my $op = '+';
print $dispatch{$op}->(2, 3), "\n";

