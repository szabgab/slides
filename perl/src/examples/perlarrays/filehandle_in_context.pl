#!/usr/bin/perl
use strict;
use warnings;

my $file = "numbers.txt";

open(my $fh, '<', $file) or die "Could not open '$file'";
# reading in SCALAR context (line by line) and processing each line
while (my $row = <$fh>) {
    chomp $row;
    print "READ: $row\n";
}


open (my $other_fh, '<', $file) or die "Could not open '$file'";
# reading in LIST context all the lines at once
my @rows = <$other_fh>;
chomp @rows;
print "READ ", scalar(@rows), " lines\n";

