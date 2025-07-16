#!/usr/bin/perl
use strict;
use warnings;

# run this script several times to see the (random) error message

use Test::More tests => 2;
use List::MoreUtils qw(any);

my @possible_values = (23, 42, 68);
{
    my $result = foo();
    is( any { $result eq $_ }, $/ );
    ok( grep { foo() eq $_ } ( 23, 42, 68 ), "name" );
}

sub foo {
    return ( ( 23, 42, 68, 100, 200 )[ rand(5) ] );
}
