#!/usr/bin/perl
use strict;
use warnings;

my $total = 0;
my $count = 0;
my $min;
my $max;

my $filename = "numbers.txt";
open(my $fh, "<", $filename) or die "Could not open '$filename'\n";
while (my $line = <$fh>) {
    chomp $line;
    $total += $line;

    if (not $count) {
        $min = $line;
        $max = $line;
    }
    $count++;

    if ($line < $min) {
        $min = $line;
    }
    if ($line > $max) {
        $max = $line;
    }
}


if (not defined $min) {
    print "No values were given\n";
} else {
    print "Min: $min   Max: $max   Total: $total   count: $count   Average: ",
          $total / $count, "\n";
}

