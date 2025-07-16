#!/usr/bin/perl
use strict;
use warnings;

use File::Find::Rule;
my $dir = '.';
if (@ARGV) {
    $dir = shift;
}

foreach my $thing (File::Find::Rule->in($dir)) {
    my @parts = split m{/}, $thing;
    print "  " x @parts;
    print "$parts[-1]\n";
}

