#!/usr/bin/perl
use strict;
use warnings;


my @files = glob "*.xml";

my @sorted_files = sort { -s $a <=> -s $b } @files;

print "@sorted_files\n";

