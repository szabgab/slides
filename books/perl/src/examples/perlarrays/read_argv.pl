#!/usr/bin/perl
use strict;
use warnings;

my $color = $ARGV[0];

if (not defined $color) {
    my @colors = ("Blue", "Yellow", "Brown", "White");

    print "Please select a number:\n";
    foreach my $i (0..$#colors) {
        print "$i) $colors[$i]\n";
    }
    my $num = <STDIN>;
    chomp($num);
    if (defined $colors[$num]) {
        $color = $colors[$num];
    } else {
        print "Bad selection\n";
        exit;
    }
}

print "The selected color is $color\n";

