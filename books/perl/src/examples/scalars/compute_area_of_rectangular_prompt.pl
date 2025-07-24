#!/usr/bin/perl
use strict;
use warnings;

print "length: ";
my $length = <STDIN>;
print "width: ";
my $width  = <STDIN>;
my $area   = $length * $width;
print "$area\n";

