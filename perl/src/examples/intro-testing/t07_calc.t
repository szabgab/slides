#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

# tell how many tests you are going to write. This is our "plan"
use Test::Simple tests => 3;

# the ok function of Test::Simple prints "ok" or "not ok"
ok `$calc 1 + 1` == 2;
ok `$calc 2 + 2` == 4;
#ok `$calc 2 + 2 + 2` == 6;

