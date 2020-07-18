#!/usr/bin/perl 
use strict;
use warnings;
use List::MoreUtils qw(uniq);

my @data = qw(Foo Bar Moose Foo Baz Bar);
my @unique = uniq @data;

print "@unique\n"; # Foo Bar Moose Baz
