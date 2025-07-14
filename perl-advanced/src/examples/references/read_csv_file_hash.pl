#!/usr/bin/perl
use strict;
use warnings;

use Data::Dumper;

my $filename = shift 
    or die "Usage: $0 FILENAME ( examples/references/data.csv )\n";

my %data;
open my $fh, '<', $filename or die;

my $header = <$fh>;
chomp $header;
my @header = split /,/, $header;

while (my $line = <$fh>) {
    chomp $line;
    my %row;
    @row{@header} = split /,/, $line;
    
    my $key = $row{fname};
    $data{$key} = \%row;
}

print Dumper \%data;

