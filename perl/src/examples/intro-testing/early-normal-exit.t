#!/usr/bin/perl
use strict;
use warnings;

# example of too few tests (less than planned)

use FindBin;

my $calc = "$FindBin::Bin/mycalc";

use Test::More tests => 4;

is `$calc 1 + 1`, 2, '1+1';
is `$calc 2 + 2`, 4, '2+2';
is `$calc 3 + 3`, 6, '3+3';
