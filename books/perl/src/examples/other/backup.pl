#!/usr/bin/perl
use strict;
use warnings;

# oss_1_12345.ARC
# oss_1_99999.ARC
# oss_1_100000.ARC

use File::Copy qw(move);

my $from = '/path/to/oss/';
my $to   = '/path/to/oss_backup/';

my @files = glob("$from/*.ARC");

my @sorted_files = sort {substr($a, 6, -4) <=> substr($b, 6, -4)} @files;

my $count = @files;
$count = 100 if @files > 100;

my @selected = @sorted_files[0..$count-1];

foreach my $file (@selected) {
	move($file, $to);
}

