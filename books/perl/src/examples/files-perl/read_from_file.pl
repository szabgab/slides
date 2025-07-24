#!/usr/bin/perl
use strict;
use warnings;

my $filename = "input.txt";
open my $fh, "<", $filename or die $!;

my $line = <$fh>;
chomp $line;

while (my $line = <$fh>) {
    chomp $line;
    #...
}



open my $data, "<", $filename or die $!;
my @lines = <$data>;
chomp @lines;
foreach my $line (@lines) {
    print $line;
}

