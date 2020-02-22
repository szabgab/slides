#!/usr/bin/perl 
use strict;
use warnings;

my $total;

add();

print "$total\n";


sub add {
    if (not defined $total) {
        $total = 0;
    }
    $total = $total + rand();
}

