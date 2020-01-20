#!/usr/bin/perl
use strict;
use warnings;

my $total = 0;
my $count = 0;
my $min;
my $max;

my $filename = "examples/files/numbers.txt";
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

open my $out, '>', 'numbers.out';
if (not defined $min) {
    print $out "No values were given\n";
} else {
    printf($out "Minimum: %5s\n", $min);
    printf($out "Maximum: %5s\n", $max);
    printf($out "Total:   %5s\n", $total);
    printf($out "Count:   %5s\n", $count);
    printf($out "Average: %5s\n", $total / $count);
}

