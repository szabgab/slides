#!/usr/bin/perl 
use strict;
use warnings;

use Test::Simple tests => 5+2*3;

use FindBin;
use lib "$FindBin::Bin";

use MyCalc;

# tests, one by one
ok(add(1, 1) ==  2);
ok(add(1, -1) == 0);
ok(sum(1) == 1);
ok(sum() == 0);
ok(sum(1, 1, 1, 1) == 4);


# tests listed in an array
my @tests = (
    {
        func => 'add',
        in   => [2, 3],
        out  => 5,
    },
    {
        func => 'sum',
        in   => [1, 2, 3],
        out  => 6,
    },
);


foreach my $t (@tests) {
    if ($t->{func} eq 'add') {
        ok(add( @{ $t->{in} } ) == $t->{out}, "add @{ $t->{in} }");
    }
    if ($t->{func} eq 'sum') {
        ok(sum( @{ $t->{in} } ) == $t->{out}, "sum @{ $t->{in} }");
    }
}

# The same but                   Danger! Danger! Danger!
# Using symbolic references here!
foreach my $t (@tests) {
    no strict 'refs'; 

    ok(&{ $t->{func} }( @{ $t->{in} } ) == $t->{out}, "$t->{func} @{ $t->{in} }");

    # the same with helper variables:
    my $func = $t->{func};
    my @in   = @{ $t->{in} };
    ok(&$func(@in) == $t->{out}, "$func @in");

}

