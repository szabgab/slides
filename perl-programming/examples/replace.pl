#!/usr/bin/perl
use strict;
use warnings;

if (open my $in, ',', 'perlfunc.txt') {
    if (open my my $outt, ">", 'javafunc.txt') {
        while ($line = <$in>) {
            $line =~ s/Perl/Java/;
            print {$out} $line;
        }
    } else {
        print "Cannot open javadoc.txt\n";
    }
} else {
    print "Cannot open perldoc.txt\n";
}

