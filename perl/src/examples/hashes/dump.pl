#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper qw(Dumper);

my %code = (
    foo => 123,
    bar => 456,
    moo => 789,
);

print Dumper \%code;

