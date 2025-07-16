#!/usr/bin/perl
use strict;
use warnings;

my @numbers = fibonacci(10);
print "@numbers\n";

sub fibonacci {
    my $num = shift;

    if ($num == 1) {
        return (1);
    } 
    if ($num == 2) {
        return (1, 1);
    }
    my @fib = (1, 1);
    foreach (3..$num) {
        push @fib, $fib[-1]+$fib[-2];
    }
    return @fib;
}
