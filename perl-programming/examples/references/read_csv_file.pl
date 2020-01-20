#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my $filename = shift 
    or die "Usage: $0 FILENAME ( examples/references/data.csv )\n";

my @data;
open my $fh, '<', $filename or die;

my $header = <$fh>;
chomp $header;
my @header = split /,/, $header;

while (my $line = <$fh>) {
    chomp $line;
    my %row;

    my @values = split /,/, $line;
    foreach my $i (0..@header-1) {
        my $field = $header[$i];
        $row{$field} = $values[$i];
    }
 
    # using hash slices:
    # @row{@header} = split /,/, $line;

    push @data, \%row;
}

print Dumper \@data;

