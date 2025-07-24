#!/usr/bin/perl
use strict;
use warnings;

if (open my $fh, '<', 'perlfunc.txt') {
    while ($line = <$fh>) {
        chomp $line;
        if ($line =~ /^(.*?)($ARGV[0])(.*)$/) {
            print "$1           <$2>           $3\n";
        }
    }
} else {
    print "Cannot open perldoc.txt\n";
}

