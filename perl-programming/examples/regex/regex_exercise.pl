#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "$0 FILENAME\n";
open my $fh, '<', $filename or die "Could not open '$filename'\n";

while (my $line = <$fh>) {
    if ($line =~ /REGEX1/) {
        print "has an a: $line";
    }

    if ($line =~ /REGEX2/) {
        print "starts with an a: $line";
    }
}
