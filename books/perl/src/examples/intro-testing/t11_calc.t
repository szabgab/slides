#!/usr/bin/perl
use strict;
use warnings;

my @tests = (
    ['1 + 1'     =>  2 ],
    ['2 + 2'     =>  4 ],
    ['2 + 2 + 2' =>  6 ],
    ['1+1'       =>  2 ],
    ['0+ -1'     => -1 ],
    ['0-1'       => -1 ],
    ['-1+1'      =>  0 ],
);

require Test::Simple;
import Test::Simple tests => scalar @tests;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

foreach my $t ( @tests ) {
    ok( `$calc $t->[0]` == $t->[1], $t->[0] );
}

