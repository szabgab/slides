#!/usr/bin/perl
use strict;
use warnings;

print "First number: ";
my $x = <STDIN>;
chomp $x;

print "Second number: ";
my $y = <STDIN>;
chomp $y;

if ($y == 0) {
    print "Cannot divide by zero\n";
} else {
    my $z = $x / $y;
    print "The result is $z\n";
}
