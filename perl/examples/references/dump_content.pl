#!/usr/bin/env perl
use strict;
use warnings;

use Data::Dumper qw(Dumper);

my @names     = qw(Foo Bar Baz);
my $names_ref = \@names;

my %phones = (
    Foo  => 123,
    Bar  => 456,
    Baz  => 789,
);
my $phones_ref = \%phones;

print Dumper $names_ref, $phones_ref;
