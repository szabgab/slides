#!/usr/bin/perl
use strict;
use warnings;

my $file = 'dna.txt';

my @dna_sequences = read_file($file);
foreach my $seq (@dna_sequences) {
    analyze_dna($seq);
}
sub analyze_dna {
    my ($dna) = @_;
    if ($dna =~ /(.)\1/) {
        print "$dna has double $1\n";
    }
}


sub read_file {
    my ($filename) = @_;
    open my $fh, '<', $filename or die;

    my @results;
    while (my $line = <$fh>) {
        chomp $line;
        if ($line =~ /^DNA:\s*([CGTA]+)/) {
            push @results, $1;
        }
    }
    return @results;
}