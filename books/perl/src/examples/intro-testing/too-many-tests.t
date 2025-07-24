#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

# example of too many tests (more than planned)

use Test::More tests => 2;

is( `$calc 1 + 1`, 2, '1+1' );
is( `$calc 2 + 2`, 4, '2+2' );
is( `$calc 3 + 3`, 6, '3+3' );

