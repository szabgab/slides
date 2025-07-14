#!/usr/bin/perl
use strict;
use warnings;

# assuming there are no R4 values then 4 substitutions will do
s/R1/R4/g
s/R3/R1/g
s/R2/R3/g
s/R4/R2/g



# or without any assumption and in one substitution:
my %map = (
    R1  => 'R2',
    R2  => 'R3',
    R3  => 'R1',
);

s/\b(R[123])\b/$map{$1}/g;


s/\b(R1|R2|R3|R12)\b/$map{$1}/g;

my $regex = join "|", keys %map;
s/\b($regex)\b/$map{$1}/g;


