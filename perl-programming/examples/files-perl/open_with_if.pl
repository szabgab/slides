#!/usr/bin/perl
use strict;
use warnings;

my $filename = "input.txt";
if (open my $in, "<", $filename) {
    # do your thing here
    # no need to explicitly close the file
} else {
    warn "Could not open file '$filename'. $!";
}
# here the $in filehandle is not accessible anymore

