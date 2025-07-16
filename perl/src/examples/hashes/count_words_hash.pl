#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";

my %count;

open(my $fh, "<", $filename)
    or die "Could not open '$filename': $!"; 
while (my $line = <$fh>) {
    chomp $line;
    my @words = split / /, $line;
    foreach my $word (@words) {
        $count{$word}++;
    }
}



foreach my $word (keys %count) {
    print "$word : $count{$word}\n";
}

