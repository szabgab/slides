#!/usr/bin/perl 
use strict;
use warnings;

my @data = qw(Foo Bar Moose Foo Baz Bar);
my @unique;
my %seen;

foreach my $value (@data) {
    if (! $seen{$value}++ ) {
        push @unique, $value;
    }
}


print "@unique\n"; # Foo Bar Moose Baz
