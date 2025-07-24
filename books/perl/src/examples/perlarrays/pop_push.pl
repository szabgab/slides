#!/usr/bin/perl
use strict;
use warnings;

my @names = ("Foo", "Bar", "Baz");

my $last_name = pop @names;

print "$last_name\n";        # Baz
print "@names\n";            # Foo Bar


push @names, "Moo";

print "@names\n";            # Foo Bar Moo
