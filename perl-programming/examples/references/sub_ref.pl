#!/usr/bin/perl
use strict;
use warnings;

sub add {
    my ($x, $y) = @_;
    return $x+$y;
}

my $add_ref = \&add;

print &{ $add_ref }(2, 3), "\n";
print $add_ref->(2, 3), "\n";

