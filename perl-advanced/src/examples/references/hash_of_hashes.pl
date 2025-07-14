#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my %distance;
$distance{'New York'}{'London'} = 5_027;
$distance{'New York'}{'Bejin'}  = 10_100;
$distance{'Paris'}{'London'}    = 350;

print Dumper \%distance;
