#!/usr/bin/perl
use strict;
use warnings;

sub incrementer {
    my $old = $_[0];
    $_[0] += $_[1];
    return $old;
}

my $x = 23;
my $old = incrementer($x, 19);
print "$old  $x\n"; # 23  42

sub incrementer_23 {
    my $inc = 23;
    my $old = $_[0];
    $_[0] += $inc;
    return $old;
}


