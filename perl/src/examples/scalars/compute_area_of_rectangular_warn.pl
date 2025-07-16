#!/usr/bin/perl
use strict;
use warnings;

print "length: ";
my $length = <STDIN>;
chomp($length);

print "width: ";
my $width = <STDIN>;
chomp($width);

if ( $length < 0 ) {
    $length = 0;
    print "WARN: The first value was negative\n";
}
if ( $width < 0 ) {
    $width = 0;
    print "WARN: The second value was negative\n";
}
my $area = $length * $width;
print "The area is $area\n";

