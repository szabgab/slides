#!/usr/bin/env perl
use strict;
use warnings;
  
# You need to parse a log file where the fields are fixed length long 
# and have no delimiters
# The definition is as follows:
# LABEL:       4 chars
# SOURCE:      8 digits
# DESTINATION: 8 digits
# TYPE:        4 chars
# VALUE:       8 digits
my $file = shift or die "Usage: $0 pack.txt\n";

open(my $data, '<', $file) or die "Could not open '$file'\n";
while (my $line = <$data>) {
    print $line;
    chomp $line;
    my ($label, $source, $dest, $type, $value) = unpack ("A4 A8 A8 A4 A8", $line);
    print "LABEL: $label SOURCE: $source DEST: $dest TYPE: $type VALUE: $value\n";
}

