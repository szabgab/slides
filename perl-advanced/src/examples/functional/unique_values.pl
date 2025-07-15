#!/usr/bin/env perl
use strict;
use warnings;

my @data = qw(Earth Mars Earth Venus Earth Mars);
my @unique;
my %seen;

foreach my $value (@data) {
    if (! $seen{$value}) {
        push @unique, $value;
        $seen{$value}++;
    }
}

print "@unique\n"; # Earth Mars Venus
