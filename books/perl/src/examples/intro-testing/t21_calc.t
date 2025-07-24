#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

use Test::More tests => 3;

ok `$calc 1 + 1` == 2,     '1+1';
ok `$calc 2 + 2` == 4,     '2+2';
ok `$calc 2 + 2 + 2` == 6, '2+2+2';

