#!/usr/bin/perl
use strict;
use warnings; 

my $s = "The black cat climbed the green tree";
my $z;
$z = substr $s, 4, 5;
print "$z\n";                         # $z = black
$z = substr $s, 4, -11;
print "$z\n";                         # $z = black cat climbed the 
$z = substr $s, 14;
print "$z\n";                         # $z = climbed the green tree
$z = substr $s, -4;
print "$z\n";                         # $z = tree
$z = substr $s, -4, 2;
print "$z\n";                         # $z = tr

$z = substr $s, 14, 7, "jumped from";
print "$z\n";                         # $z = climbed
print "$s\n";          # $s = The black cat jumped from the green tree

