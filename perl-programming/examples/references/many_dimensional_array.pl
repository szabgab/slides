#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my @dim;
$dim[0] = "zero";
$dim[1][0] = "one-zero";
$dim[1][1][1] = "one-one-one";
$dim[2][0][0] = "two-zero-zero";

print Dumper \@dim;
