#!/usr/bin/perl
use strict;
use warnings;

my $dir = shift or die "Usage: $0 DIRECTORY\n";

opendir my $dh, $dir or die "Cannot open $dir: $!\n";
while (my $entry = readdir $dh) {
    if ($entry eq "." or $entry eq "..") {
        next;
    }
    print "$entry\n";
}
closedir $dh;

