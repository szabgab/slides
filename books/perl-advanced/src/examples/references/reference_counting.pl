#!/usr/bin/env perl
use strict;
use warnings;
use Devel::Refcount qw(refcount);

my $names_ref;

{
    my @names = qw(Foo Bar);
    $names_ref = \@names;
}
print "$names_ref->[0]\n"; # Foo
print(refcount($names_ref), "\n"); # 1

