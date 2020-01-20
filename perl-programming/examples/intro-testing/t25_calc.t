#!/usr/bin/perl
use strict;
use warnings;

use FindBin;
my $calc = "$FindBin::Bin/mycalc";

use Test::More tests => 1;

is `$calc "2 * 2"`, 4, '2*2';

