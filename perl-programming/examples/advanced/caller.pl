#!/usr/bin/perl
use strict;
use warnings;

fib(4);

sub fib {
    my $n = shift;
    my ($package, $filename, $line) = caller(0);
    print "$package  $filename  $line\n";
    if ($n == 1 or $n == 2) {
        return 1;
    }
    return fib($n-1) + fib($n-2);
}
