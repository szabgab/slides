#!/usr/bin/perl
use strict;
use warnings;

# data: field_value_pairs.txt
my $filename = shift or die "Usage: $0 filename\n";

open(my $fh, "<", $filename) or die "Could not open '$filename'\n";
while (my $line = <$fh>) {
    chomp $line;
    my ($field, $value) = split /\s*=\s*/, $line;
    print "$value=$field\n";
}
