#!/usr/bin/env perl
use strict;
use warnings FATAL => 'all';

my @data = qw(Earth Mars Earth Venus Earth Mars);

#my %seen;
#my @unique = grep { !$seen{$_}++ } @data;

my @unique = do { my %seen; grep { !$seen{$_}++ } @data };

print "@unique\n"; # Earth Mars Venus
