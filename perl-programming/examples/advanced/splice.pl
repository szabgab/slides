#!/usr/bin/perl
use strict;
use warnings;

my @names = qw(Foo Bar Baz Moo Qux Barney Hoppy Bammbamm Dino);
my @more_names = qw(Fred Wilma);

my @sublist = splice(@names, 2, 3);
print "@sublist\n";              # Baz Moo Qux
print "@names\n";                # Foo Bar Barney Hoppy Bammbamm Dino

my @zlist = splice(@names, 2, 3, @more_names);
print "@zlist\n";                # Barney Hoppy Bammbamm
print "@names\n";                # Foo Bar Fred Wilma Dino

