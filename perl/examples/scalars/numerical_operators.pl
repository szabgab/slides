#!/usr/bin/perl
use strict;
use warnings;

my $x = 3;
my $y = 11;

my $z = $x + $y;
print "$z\n";         # 14

$z = $x * $y;
print "$z\n";         # 33
print $y / $x, "\n";  # 3.66666666666667

$z = $y % $x;         # (modulus)
print "$z\n";         # 2

$z += 14;             # is the same as   $z = $z + 14;
print "$z\n";         # 16

$z++;                 # is the same as   $z = $z + 1;
$z--;                 # is the same as   $z = $z - 1;

$z = 23 ** 2;         # exponentiation
print "$z\n";         # 529

