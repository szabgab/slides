#!/usr/bin/env perl
use strict;
use warnings;

my @names = qw(Foo Bar);
my $names_ref = \@names;

$names_ref->[0] = 'Baz';
print "$names[0]\n";        # Baz
print "$names_ref->[0]\n";  # Baz

