#!/usr/bin/perl
use strict;
use warnings;

my $filename = "input.txt";
open(my $fh, "<", $filename) or die "Could not open '$filename'\n";
while (my $line = <$fh>) {
    print $line;
}

