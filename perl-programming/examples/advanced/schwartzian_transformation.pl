#!/usr/bin/perl
use strict;
use warnings;

my @files = glob "*.xml";

my @quickly_sorted_files =
    map  { $_->[0] }
    sort { $a->[1] <=> $b->[1] }
    map  { [$_, -s $_] }
    @files;

print "@quickly_sorted_files\n";

