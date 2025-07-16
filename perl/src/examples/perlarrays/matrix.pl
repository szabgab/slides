#!/usr/bin/perl
use strict;
use warnings;

my @matrix;

$matrix[0][0] = 0;
$matrix[1][1] = 11;
$matrix[1][2] = 12;

#print "$matrix\n";
print "$matrix[0]\n";                 # ARRAY(0x814dd90)
print "$matrix[1][1]\n";              # 11

use Data::Dumper qw(Dumper);
print Dumper \@matrix;
