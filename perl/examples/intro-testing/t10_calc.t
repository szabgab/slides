#!/usr/bin/perl
use strict;
use warnings;

use FindBin;

my @tests = (
    ['1 + 1'     =>  2 ],
    ['2 + 2'     =>  4 ],
    ['2 + 2 + 2' =>  6 ],
    ['1+1'       =>  2 ],
    ['0+ -1'     => -1 ],
    ['0-1'       => -1 ],
    ['-1+1'      =>  0 ],
);

use Test::Simple tests => 7;

foreach my $t ( @tests ) {
    ok( `$FindBin::Bin/mycalc $t->[0]` == $t->[1], $t->[0] );
}

