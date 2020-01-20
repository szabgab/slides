#!/usr/bin/perl
use strict;
use warnings;

print "First number: ";
my $x = <STDIN>;
chomp $x;

print "Second number: ";
my $y = <STDIN>;
chomp $y;

my $z = $x / $y;
print "The result is $z\n";
