#!/usr/bin/env perl
use v5.10;
use strict;
use warnings;

my $x;
my @y;

our $xx;

foreach my $variable (sort keys %main::) {
    say $variable;
}
