#!/usr/bin/perl 
use strict;
use warnings FATAL => 'all';

my @data = qw(Foo Bar Moose Foo Baz Bar);

#my %seen;
#my @unique = grep { !$seen{$_}++ } @data;


my @unique = do { my %seen; grep { !$seen{$_}++ } @data };

print "@unique\n"; # Foo Bar Moose Baz
