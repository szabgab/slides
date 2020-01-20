#!/usr/bin/perl
use strict;
use warnings;

my $x = 7;

# Postfix ++ increments AFTER the OLD value was used
my $y = $x++;  
print "y = $y, x = $x\n";     # y = 7,  x = 8,


$x = 7;

$y = ++$x; 
print "y = $y, x = $x\n";     # y = 8, x = 8
