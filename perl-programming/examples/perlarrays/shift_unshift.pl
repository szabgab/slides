#!/usr/bin/perl
use strict;
use warnings;

my @names = ("Foo", "Bar", "Baz");
my $first = shift @names;

print "$first\n";              # Foo
print "@names\n";              # Bar Baz



unshift @names, "Moo";
print "@names\n";              # Moo Bar Baz

