#!/usr/bin/perl
use strict;
use warnings;

my $filename = "input.txt";
open(my $fh, "<", $filename) or die "Could not open file '$filename'. $!";
# do your thing here
close $fh;

