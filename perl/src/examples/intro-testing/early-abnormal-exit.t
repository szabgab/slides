#!/usr/bin/perl 
use strict;
use warnings;

# example of tests where the script dies before running all the tests

use FindBin;

my $calc = "$FindBin::Bin/mycalc";

use Test::More tests => 4;

is `$calc 1 + 1`, 2, '1+1';
is `$calc 2 + 2`, 4, '2+2';
exit;
is `$calc 3 + 3`, 6, '3+3';
is `$calc 4 + 4`, 8, '4+4';
