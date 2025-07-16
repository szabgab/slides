#!/usr/bin/perl
use strict;
use warnings;

my $file = 'process_csv_file.csv';
if (defined $ARGV[0]) {
    $file = $ARGV[0];
}
   
my $sum = 0;
open(my $data, '<', $file) or die "Could not open '$file' $!\n";
while (my $line = <$data>) {
    chomp $line;

    my @fields = split /;/, $line;
    $sum += $fields[2];
}
print "$sum\n";

