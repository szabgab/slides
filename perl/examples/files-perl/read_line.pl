#!/usr/bin/perl
use strict;
use warnings;

# Reading a line from a file (or rather from a filehandle)
my $filename = "input.txt";
if (open my $data, "<", $filename) {
    my $line = <$data>; 
    print $line;

} else {
    warn "Could not open file '$filename': $!";
}

