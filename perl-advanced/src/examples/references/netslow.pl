#!/usr/bin/perl
use strict;
use warnings;

use lib 'examples/references';
use NetSlow qw(compute);

die "Need 2 numbers\n" if @ARGV != 2;

print compute(@ARGV), "\n";
