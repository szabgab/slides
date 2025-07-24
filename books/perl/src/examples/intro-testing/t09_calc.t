#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

use Test::Simple tests => 3;

ok `$calc 1 + 1` == 2,     'small sum: 1+1';
ok `$calc 2 + 2` == 4,     'small sum: 2+2';
ok `$calc 2 + 2 + 2` == 6, 'two operators: 2+2+2';

