#!/usr/bin/perl 
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";

open(my $fh, "<", $filename)
    or die "Could not open '$filename': $!";

my @numbers;
while (my $line = <$fh>) {
    chomp $line;
    my @num = split / /, $line;
    push @numbers, @num;
}

my @sorted = sort {$a <=> $b} @numbers;

foreach my $n (@sorted) {
    print "$n\n";
}

