#!/usr/bin/perl
use strict;
use warnings;

my $file = 'examples/input_validation.txt';
if (@ARGV) {
    $file = shift;
}
open(my $data, '<', $file) or die "Could not open '$file'\n";

while (my $line = <$data>) {
    chomp $line;
    print "LINE: '$line'";
    if ($line =~ /^\s*$/) {                    # $line !~ /\S/
        print "  row with white spaces";
    } 
    if ($line =~ /^[+-]?\d+(\.\d+)?$/) {
        print "  number";
    } 
    if ($line =~ /^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$/) {
        print "  IP addres";
    }
    if ($line =~ /(\w)\1/) {
        print "  double letter '$1'";
    }
    if ($line =~ /(\w{4,}).*\1/) {
        print "  repetition of 4 or longer '$1'";
    }
    print "\n";
}
