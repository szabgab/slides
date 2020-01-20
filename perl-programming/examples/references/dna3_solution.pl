#!/usr/bin/perl
use strict;
use warnings;

my $file = 'dna.txt';

my @dna_sequences = read_file(\&analyze_dna, $file);
sub analyze_dna {
    my ($dna) = @_;
    if ($dna =~ /(.)\1/) {
        print "$dna has double $1\n";
        return 1
    }

    return 0;
}

sub read_file {
    my ($sub, $filename) = @_;
    open my $fh, '<', $filename or die;

    while (my $line = <$fh>) {
        chomp $line;
        if ($line =~ /^DNA:\s*([CGTA]+)/) {
            last if $sub->($1);
        }
    }
    return;
}
