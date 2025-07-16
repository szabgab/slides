#!/usr/bin/perl
use strict;
use warnings;
use v5.10;

my @stack;
while (1) {

    print '$ ';
    my $in = <STDIN>;
    chomp $in;

    given ($in) {
        when ("q") { last; }
        when ("c") { 
            pop @stack; 
            }   # fetch the last value
        when ("*") { 
            my $x = pop(@stack);
            my $y = pop(@stack);
            push(@stack, $x*$y);
            }
        when ("+") { 
            my $x = pop(@stack);
            my $y = pop(@stack);
            push(@stack, $x + $y);
            }
        when ("/") {
            my $x = pop(@stack);
            my $y = pop(@stack);
            push(@stack, $y /  $x); 
            }
        when ("-") { 
            my $x = pop(@stack);
            my $y = pop(@stack);
            push(@stack, $y - $x);
            }
        when ("=") { 
            print pop(@stack), "\n"; 
            }
        default { push @stack, $in; }
    }
}

