#!/usr/bin/perl
use strict;
use warnings;

my $file = 'sort_mixed_strings.txt';
if (@ARGV) {
    $file = shift;
}
open(my $fh, '<', $file) or die "Could not open '$file'\n";

my @data = <$fh>;
chomp @data;

my @sorted = sort { 
            substr($a, 0, 1) cmp substr($b, 0, 1) 
            or
            substr($a, 1) <=> substr($b, 1) } @data;
foreach my $v (@sorted) {
    print "$v\n";
}

