#!/usr/bin/perl
use strict;
use warnings;

# given a file with a number on each row, print the sum of the numbers

my $sum = 0;
my $filename = "numbers.txt";
open(my $fh, "<", $filename) or die "Could not open '$filename'\n";
while (my $line = <$fh>) {
    $sum += $line;
}
print "The total value is $sum\n";
