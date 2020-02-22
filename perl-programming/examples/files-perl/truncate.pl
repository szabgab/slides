#!/usr/bin/perl
use strict;
use warnings;

my $new = $ARGV[0];

my $filename = "file.txt";
open my $fh, "+<", $filename or die "Could not open $!\n";
my $old = <$fh>;

seek $fh, 0, 0;              # move to the beginning of the file 
print $fh $new;
truncate $fh, length $new;   # cut the file to the new size

