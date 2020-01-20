#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

use Test::More tests => 3;

is `$calc 1 + 1`,     2, '1+1';
is `$calc 2 + 2`,     4, '2+2';
is `$calc 2 + 2 + 2`, 6, '2+2+2';

