#!/usr/bin/perl
use strict;
use warnings;

my $file = 'dna.txt';

my @dna_sequences = read_file(\&analyze_dna, $file);
sub analyze_dna {
    my ($dna) = @_;
    if ($dna =~ /(.)\1/) {
        print "$dna has double $1\n";
    }
}

sub read_file {
    ...
    return;
}
