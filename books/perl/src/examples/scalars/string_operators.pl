#!/usr/bin/perl
use strict;
use warnings;

my $x = "Hello";
my $y = "World";

# . is the concatenation operator, ataching ons string after the other
my $z = $x . " " . $y;  #       the same as "$x $y"
print $z, "\n";         # Hello World

my $w = "Take " . (2 + 3);     # you cannot write "Take (2 + 3)" here
print "$w\n";           # Take 5

$z .= "! ";             #       the same as  $z = $z . "! ";
print "'$z'\n";         # 'Hello World! '

# x is the string repetition operator
my $q = $z x 3;
print "'$q'\n";         # 'Hello World! Hello World! Hello World! '

