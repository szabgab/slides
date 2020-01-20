#!/usr/bin/perl
use strict;
use warnings;

use File::Slurp qw(slurp);

my $filename = $ARGV[0];
if (not defined $filename) {
    die "Usage: $0 FILENAME\n";
}

my $text = slurp($filename);


my @lines = slurp($filename);

