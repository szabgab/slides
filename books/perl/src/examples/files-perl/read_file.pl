#!/usr/bin/perl
use strict;
use warnings;

# reading in 30 characters:

open my $in, "<", $0 or die $!;
my $expected = 30;
my $buf;
my $actual = read $in, $buf, $expected;
if ($actual < $expected) {
    print "reached end of file\n";
}

