#!/usr/bin/env perl
use strict;
use warnings;

my $names_ref;

{
    my @names = qw(Foo Bar);
    $names_ref = \@names;
}
print "$names_ref->[0]\n"; # Foo
# print "@names\n";  # Global symbol "@names" requires explicit package name

