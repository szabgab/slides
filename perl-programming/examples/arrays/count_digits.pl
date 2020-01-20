#!/usr/bin/perl
use strict;
use warnings;

my $filename = shift or die "Usage: $0 filename\n";

my @count;

open(my $fh, "<", $filename)
    or die "Could not open '$filename': $!";

while (my $line = <$fh>) {
    chomp $line;
    my @chars = split //, $line;
    foreach my $c (@chars) {
        if ($c ne " ") {
            $count[$c]++;
        }
    }
}

foreach my $i (0..9) {
    print "$i ", ($count[$i] ? $count[$i] : 0), "\n";
}

