#!/usr/bin/perl
use strict;
use warnings;

my $x = 5;        # 00101
my $y = 3;        # 00011

my $z = $x & $y;  # 00001    = 1

$z = $x | $y;     # 00111    = 7

$z = $x ^ $y;     # 00110    = 6

$z = ~ 1;         # 11111111111111111111111111111110   (32 chars)  = 4294967294


$z = $x << 2;     # 10100    = 20

$z = $x >> 2;     # 00001    = 1

printf "%b", $x; # in order to print the binary form of a value

### Bitwise operators on strings
$a = "h l o";
$b = " e l ";
print $a | $b, "\n";
print $a ^ $b, "\n";

# hello
# HELLO
