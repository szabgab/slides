#!/usr/bin/perl
use strict;
use warnings;

my $add_ref = sub {
    my ($x, $y) = @_;
    return $x+$y;
};

print &{ $add_ref }(2, 3), "\n";
print $add_ref->(2, 3), "\n";

