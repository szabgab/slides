#!/usr/bin/perl
use strict;
use warnings;

if (open my $fh, '<', 'perlfunc.txt') {
    while ($line = <$fh>) {
        if ($line =~ /$ARGV[0]/) {
            print $line;
        }
    }
} else {
    print "Cannot open perldoc.txt\n";
}

