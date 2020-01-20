#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";
open(my $fh, "<", $filename) or die "Could not open '$filename'\n";

my @snmps = <$fh>;
chomp @snmps;

print join "\n", @snmps;
print "\n------------------\n";
my @sorted_snmps = sort { cmp_snmp($a, $b) } @snmps;
print join "\n", @sorted_snmps;

sub cmp_snmp {
    my ($first, $second) = @_;

    if ($first eq $second) {
        return 0;
    }

    my @F = split /\./, $first;
    my @S = split /\./, $second;
    
    foreach my $i (0..@F-1) { 
        if ($i >= @S) {
            return 1;
        }
        if ($F[$i] < $S[$i]) {
            return -1;
        }
        if ($F[$i] > $S[$i]) {
            return 1;
        }
    }
    return -1;
}

print "\n------------------\n";

