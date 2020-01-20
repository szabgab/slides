#!/usr/bin/perl
use strict;
use warnings;


my @files = glob "*.xml";

my @unsorted_pairs = map  { [$_, -s $_] } @files;
my @sorted_pairs   = sort { $a->[1] <=> $b->[1] } @unsorted_pairs;
my @quickly_sorted_files = map  { $_->[0] } @sorted_pairs;

print "@quickly_sorted_files\n";

