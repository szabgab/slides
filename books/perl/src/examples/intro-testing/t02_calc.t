#!/usr/bin/perl
use strict;
use warnings;

use FindBin;

my $calc = "$FindBin::Bin/mycalc";

system "$calc 1  + 1";
print " 2\n";
system "$calc 2 + 2";
print " 4\n";
system "$calc 2 + 2 + 2";
print " 6\n";

