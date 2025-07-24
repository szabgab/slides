#!/usr/bin/perl
use strict;
use warnings;

my @files = glob "*.xml";
my @old_files = grep { -M $_ > 365 } @files;
print join "\n", @old_files;
