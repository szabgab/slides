#!/usr/bin/perl 
use strict;
use warnings;

my $total;

add();

print "$total\n";


sub add {
    no warnings 'uninitialized';
    $total = $total + rand();
}
