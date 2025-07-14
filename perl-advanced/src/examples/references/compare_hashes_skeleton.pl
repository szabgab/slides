#!/usr/bin/env perl
use strict;
use warnings;

my %x = (
    foo    => 1,
    bar    => 2,
    baz    => 3,
    zoo    => 6,
    foobar => undef,
    moose  => undef,
);
my %y = (
    foo    => 1,
    bar    => 4,
    moo    => 5,
    zoo    => undef,
    foobar => 9,
    moose  => undef,
);

my @report = compare_hashes(\%x, \%y);
print join "\n", @report;
print "\n";
