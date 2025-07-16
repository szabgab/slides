#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

system "$calc 1  + 1";
print "\n";
system "$calc 2 + 2";
print "\n";
system "$calc 2 + 2 + 2";
print "\n";

