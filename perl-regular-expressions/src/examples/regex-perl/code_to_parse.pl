#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";
open(my $fh, "<", $filename) or die "Could not open '$filename'\n";

my @snmps = <$fh>;
chomp @snmps;

print join "\n", @snmps;
print "\n------------------\n";
my @sorted_snmps = sort by_snmp_number @snmps;
print join "\n", @sorted_snmps;

sub by_snmp_number {
    return 0 if $a eq $b;
    my @a = split /\./, $a;
    my @b = split /\./, $b;
    foreach my $i (0..@a-1) { 
        return 1 if $i >= @b;
        next if $a[$i] == $b[$i];
        return $a[$i] <=> $b[$i];
    }
    return -1;
}

print "\n------------------\n";

